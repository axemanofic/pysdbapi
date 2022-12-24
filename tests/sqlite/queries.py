from typing import OrderedDict, Union

from pysdbapi import DBApi, DataBase

from .consts import DATABASE_SETTINGS

db = DBApi(DataBase.SQLITE, DATABASE_SETTINGS)


@db.execute_sql()
def get_posts() -> OrderedDict[str, Union[str, int]]:
    return """
    SELECT title, text
    FROM posts
    """


@db.execute_sql()
def get_post_by_id(pk: int) -> OrderedDict[str, Union[str, int]]:
    return """
    SELECT id, title, text
    FROM posts WHERE id = ?
    """, (
        pk,
    )


@db.execute_sql(show_table=True)
def get_all_posts__table() -> OrderedDict[str, Union[str, int]]:
    return """SELECT * FROM posts"""
