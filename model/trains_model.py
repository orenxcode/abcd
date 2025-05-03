import sqlite3

class Trains:

    @staticmethod
    def get_all_trains():
        with sqlite3.connect("db/trainsDB.db") as connection:
            cursor=connection.cursor()
            sql="""SELECT 
            trains.id, 
            trains.name, 
            trains.engine, 
            trains.speed, 
            trains.route, 
            trains.type, 
            trains.line_id,
            lines.name,
            lines.status
            FROM trains INNER JOIN lines ON trains.line_id=lines.id"""
            cursor.execute(sql)
            rows=cursor.fetchall()
            cursor.close()
        return rows
    

    @staticmethod
    def get_all_lines():
        with sqlite3.connect("db/trainsDB.db") as connection:
            cursor=connection.cursor()
            sql="""SELECT * FROM lines"""
            cursor.execute(sql)
            rows=cursor.fetchall()
            cursor.close()
        return rows
    
