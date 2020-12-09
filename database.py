from flask import g
import sqlite3
import os


basedir = os.path.abspath(os.path.dirname(__file__))
DB_NAME = os.path.join(basedir, 'flaskApi.db')

def connect_db():
    sql = sqlite3.connect(DB_NAME)
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db