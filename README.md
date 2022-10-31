# pysdbapi

[![Dependencies](https://img.shields.io/librariesio/github/axemanofic/pysdbapi)](https://pypi.org/project/pysdbapi/)
[![Version](https://img.shields.io/pypi/v/pysdbapi?color=green)](https://pypi.org/project/pysdbapi/)
[![Downloads](https://pepy.tech/badge/pysdbapi/month)](https://pepy.tech/project/pysdbapi)
[![Downloads](https://pepy.tech/badge/pysdbapi/week)](https://pepy.tech/project/pysdbapi)

pySDBAPI - simple database API. Use a couple of lines to make a request

## Features

* Use a single decorator to complete a request. Receive OrderedDict immediately in response.
* If you need to display the table in the console, then use the __show_table__ parameter
* So far only SQLite is supported, support for other databases (MySQL, PostgreSQL and others) will be added in the future

## Installation

```text
poetry add pysdbapi
```

or

```text
pip install pysdbapi
```

### Optional dependencies

This dependency is needed to print the table to the console

```text
poetry add pysdbapi[pretty]
```

## Example SQLite

This code sends a message on your behalf to the chat

```python
import pysdbapi

DATABASE_SETTINGS = {"database": "test.db"}

db = pysdbapi.DBApi(DATABASE_SETTINGS)

@db.execute_sql()
def get_all_posts():
    return """SELECT * FROM posts"""


@db.execute_sql(show_table=True)
def get_all_posts__table():
    return """SELECT * FROM posts"""
```

Result:

```
# Example show table

+----+-----------+----------------------+
| id |   title   |         text         |
+----+-----------+----------------------+
| 1  | Article 1 | Some text in article |
| 2  | Article 2 | Some text in article |
| 3  | Article 3 | Some text in article |
| 4  | Article 4 | Some text in article |
| 5  | Article 5 | Some text in article |
| 6  |   dasdas  |       sddsdas        |
+----+-----------+----------------------+
```
