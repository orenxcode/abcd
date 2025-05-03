import sqlite3

class TrainsSetup:

    @staticmethod
    def create_table_trains():
        with sqlite3.connect("db/trainsDB.db") as connection:
            cursor=connection.cursor()
            sql="""CREATE TABLE IF NOT EXISTS trains (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                engine TEXT,
                speed INTEGER,
                route TEXT,
                type TEXT,
                line_id INTEGER)"""
            cursor.execute(sql)
            cursor.close()
        return "Trains table has been created."


@staticmethod
def create_table_lines():
    with sqlite3.connect("db/trainsDB.db") as connection:
        cursor=connection.cursor()
        sql="""CREATE TABLE IF NOT EXISTS lines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            status TEXT)"""
        cursor.execute(sql)
        cursor.close()
    return "Lines table has been created."


@staticmethod
def insert_lines(name,status):
    with sqlite3.connect("db/trainsDB.db") as connection:
        cursor=connection.cursor()
        sql="""INSERT INTO lines (
        name,
        status) 
        VALUES (?,?)"""
        cursor.execute(sql,(name,status))
        last_line=cursor.lastrowid
        cursor.close()
    return f"Line {last_line} has been inserted."

