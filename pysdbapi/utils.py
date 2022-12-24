from collections import OrderedDict
from typing import Optional
from enum import Enum
from types import ModuleType

from .type_hints import CursorAlias
from .database import DataBase


def get_list_ordereddict(cursor: CursorAlias) -> Optional[list[OrderedDict]]:
    if cursor.description:
        columns: list[str] = [column[0] for column in cursor.description]
        return [OrderedDict(zip(columns, row)) for row in cursor.fetchall()]
    return None


def get_database(db_value: Enum) -> ModuleType:
    try:
        if db_value == DataBase.MSSQL:
            import pyodbc as db
        elif db_value == DataBase.PSQL:
            import psycopg2 as db
        elif db_value == DataBase.MYSQL:
            import mysql.connector as db
        elif db_value == DataBase.SQLITE:
            import sqlite3 as db
        else:
            raise Exception(f"Selected module not found {db_value.__str__()}") 
    except (ImportError, ModuleNotFoundError):
        raise Exception(f"Error load module {db_value.value}")
    return db
