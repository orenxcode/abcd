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
                port INTEGER UNIQE,
                line_id INTEGER)"""
            cursor.execute(sql)
            cursor.close()
        return "Trains table has been created."


    @staticmethod
    def insert_trains (name,engine,speed,route,type,line_id):
        with sqlite3.connect("db/trainsDB.db") as connection:
            cursor=connection.cursor()
            sql="""SELECT port FROM trains"""
            cursor.execute(sql)
            rows=cursor.fetchall()
            list_of_ports=[]
            for i in rows:
                port1=i[0]
                list_of_ports.append(port1)
            for i in range (1,21):
                if i not in list_of_ports:
                    port=i
                    count=1
                    break
            if count!=1:
                port=999

            sql="""INSERT INTO trains (
                name,
                engine,
                speed,
                route,
                type,
                port,
                line_id) 
                VALUES (?,?,?,?,?,?,?)"""
            cursor.execute(sql,(name,engine,speed,route,type,port,line_id))
            last_train=cursor.lastrowid
            cursor.close()
        return f"Train {last_train} has been inserted. Port: {port}"


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

