from typing import Any, Callable, OrderedDict, Union, Type
from enum import Enum

from .type_hints import *
from .utils import *
from .exceptions import ModulePrettyTableNotFound

class DBApi:
    def __init__(self, db: Enum, settings: dict[str, Union[str, int]]) -> None:
        self.db = get_database(db)
        self.settings: dict = settings

    def __get_sql(
        self, get_query: DecoratedCallable, *args: tuple, **kwargs: dict
    ) -> tuple[str, tuple]:
        sql: str = ""
        params: tuple = tuple()
        try:
            sql, params = get_query(*args, **kwargs)
        except ValueError:
            sql = get_query()
        return sql, params

    def __execute(
        self,
        get_result: Callable[[CursorAlias], ExecutorResult],
        sql: str,
        params: tuple,
    ) -> ExecutorResult:
        try:
            connection = self.db.connect(**self.settings)
            cursor = connection.cursor()
            cursor.execute(sql, params)
            result: ExecutorResult = get_result(cursor)
        except Exception as e:
            raise e
        else:
            connection.commit()
        finally:
            connection.close()
        return result

    def execute_sql(self, show_table: bool = False):
        def wrapper(get_query):
            def main(*args: P.args, **kwargs: P.kwargs) -> ExecutorResult:
                sql, params = self.__get_sql(get_query, *args, **kwargs)
                if show_table:
                    try:
                        from prettytable import from_db_cursor
                    except (ImportError, ModuleNotFoundError):
                        raise Exception("Module 'prettytable' prettytable not installed")
                    else:
                        return self.__execute(from_db_cursor, sql, params)
                return self.__execute(get_list_ordereddict, sql, params)

            return main

        return wrapper
