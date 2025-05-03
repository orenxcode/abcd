from model.trains_model import Trains
from service.trains_service import TrainsService


class TrainsController:


    @staticmethod
    def get_all_trains_controller():
        result=Trains.get_all_trains()
        rows=[]
        for i in result:
            row={
                "id":i[0],
                "name":i[1],
                "engine":i[2],
                "speed":i[3],
                "route":i[4],
                "type":i[5],
                "port":i[6],
                "line_id":i[7],
                "line_name":[8],
                "line_status":i[9],
                "rank":TrainsService.calculate_rank_trains(i[3])
                }
            rows.append(row)
        return rows
    

    @staticmethod
    def get_all_lines_controller():
        result=Trains.get_all_lines()
        rows=[]
        for i in result:
            row={"id":i[0],"name":i[1],"status":i[2]}
            rows.append(row)
        return rows
    

    @staticmethod
    def get_one_by_id_trains_controller(id):
        result=Trains.get_one_by_id_trains(id)
        row={
            "id":result[0],
            "name":result[1],
            "engine":result[2],
            "speed":result[3],
            "route":result[4],
            "type":result[5],
            "port":result[6],
            "line_id":result[7],
            "line_name":result[8],
            "line_status":result[9],
            "rank":TrainsService.calculate_rank_trains(result[3])}
        return row
    

    @staticmethod
    def update_speed_by_id_trains_controller(id,speed):
        result=Trains.update_speed_by_id_trains(id,speed)
        return result
    

    @staticmethod
    def delete_by_id_trains_controller(id):
        result=Trains.delete_by_id_trains(id)
        return result
    

    @staticmethod
    def get_train_line_status_controller():
        result=Trains.get_train_line_status()
        rows=[]
        for i in result:
            row={"train_name":i[0],"line_name":i[1],"line_status":i[2]}
            rows.append(row)
        return rows
    

    @staticmethod
    def get_trains_lines_active_controller():
        result=Trains.get_trains_lines_active()
        rows=[]
        for i in result:
            row={
                "id":i[0],
                "name":i[1],
                "engine":i[2],
                "speed":i[3],
                "route":i[4],
                "type":i[5],
                "port":i[6],
                "line_id":i[7],
                "line_name":i[8],
                "line_status":i[9]}
            rows.append(row)
        return rows
    

