import random
import sqlite3

import pytest

from pysdbapi.exceptions import ModulePrettyTableNotFound

from .consts import *
from .queries import *


class DataBase:
    def init_db(self):
        try:
            connection = sqlite3.connect(**DATABASE_SETTINGS)
            cursor = connection.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    text TEXT
                )
                """
            )

            cursor.execute("SELECT * FROM posts")
            posts = cursor.fetchall()
            if not posts:
                cursor.executemany("INSERT INTO posts VALUES (NULL, ?, ?)", POSTS)
        except Exception as e:
            raise e
        else:
            connection.commit()
        finally:
            connection.close()
        return 1

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(DataBase, cls).__new__(cls)
            cls.instance.init_db()
        return cls.instance


@pytest.fixture
def database():
    return DataBase()


@pytest.fixture
def pk():
    return random.randint(1, 5)


def test_get_all_posts(database):
    posts = get_posts()
    assert posts == ALL_POSTS


def test_get_post_by_id(database, pk):
    random_post = {"id": pk, "title": f"Article {pk}", "text": "Some text in article"}
    post = get_post_by_id(pk)[0]
    assert post == random_post


def test_get_all_posts__table(database):
    try:
        posts = get_all_posts__table()
    except Exception as e:
        assert (
            e.__str__()
            == "Requires `prettytable` to be installed. Use 'pip install prettytable'"
        )
    else:
        from prettytable import PrettyTable

        assert isinstance(posts, PrettyTable)
