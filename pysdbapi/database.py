from enum import Enum


class DataBase(Enum):
    MSSQL = 'pyodbc'
    PSQL = 'psycopg2'
    MYSQL = 'mysql'
    SQLITE = 'sqlite3'
