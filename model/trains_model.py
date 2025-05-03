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
            trains.port, 
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
    

    @staticmethod
    def get_one_by_id_trains(id):
        with sqlite3.connect("db/trainsDB.db") as connection:
            cursor=connection.cursor()
            sql="""SELECT 
                trains.id, 
                trains.name, 
                trains.engine, 
                trains.speed, 
                trains.route, 
                trains.type,
                trains.port, 
                trains.line_id,
                lines.name,
                lines.status
                FROM trains INNER JOIN lines ON trains.line_id=lines.id
                WHERE trains.id=?"""
            cursor.execute(sql,(id,))
            row=cursor.fetchone()
            cursor.close()
        return row
    

    @staticmethod
    def update_speed_by_id_trains(id,speed):
        with sqlite3.connect("db/trainsDB.db") as connection:
            cursor=connection.cursor()
            sql="""SELECT id FROM trains
                WHERE id=?"""
            cursor.execute(sql,(id,))
            row=cursor.fetchone()
            if row is None:
                cursor.close()
                return "ID was not found"
            else:
                sql="""UPDATE trains
                    SET speed=?
                    WHERE id=?"""
                cursor.execute(sql,(speed,id))
                last_update=cursor.lastrowid
                cursor.close()
                return f"Train ID: {last_update} / Status: Updated."


    @staticmethod
    def delete_by_id_trains(id):
        with sqlite3.connect("db/trainsDB.db") as connection:
            cursor=connection.cursor()
            sql="""SELECT id FROM trains
                WHERE id=?"""
            cursor.execute(sql,(id,))
            row=cursor.fetchone()
            if row is None:
                cursor.close()
                return "ID was not found"
            else:
                sql="""DELETE FROM trains
                    WHERE id=?"""
                cursor.execute(sql,(id,))
                last_delete=cursor.lastrowid
                cursor.close()
                return f"Train ID: {last_delete} / Status: Deleted."
        

    @staticmethod
    def get_train_line_status():
        with sqlite3.connect("db/trainDB.db") as connection:
            cursor=connection.cursor()
            sql="""SELECT
                trains.name,
                lines.name,
                lines.status
                FROM trains INNER JOIN lines ON trains.id=lines.id"""
            cursor.execute(sql)
            rows=cursor.fetchall()
            cursor.close()
        return rows
    

    @staticmethod
    def get_trains_active_lines():
        with sqlite3.connect("db.trainsDB.db") as connection:
            cursor=connection.cursor()
            sql="""SELECT
                trains.id, 
                trains.name, 
                trains.engine, 
                trains.speed, 
                trains.route, 
                trains.type,
                trains.port, 
                trains.line_id,
                lines.name,
                lines.status
                FROM trains INNER JOIN lines ON trains.line_id=lines.id
                WHERE lines.status='active'
                """
            cursor.execute(sql)
            rows=cursor.fetchall()
            cursor.close()
        return rows
    
