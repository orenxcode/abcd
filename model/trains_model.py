import sqlite3

class Trains:

    @staticmethod
    def insert_trains (name,engine,speed,route,type,line_id):
        with sqlite3.connect("db/trainsDB.db") as connection:
            cursor=connection.cursor()
            sql="""INSERT INTO trains (
                name,
                engine,
                speed,
                route,
                type,
                line_id) 
                VALUES (?,?,?,?,?,?)"""
            cursor.execute(sql,(name,engine,speed,route,type,line_id))
            last_train=cursor.lastrowid
            cursor.close()
        return f"Train {last_train} has been inserted."
    
    
    
    