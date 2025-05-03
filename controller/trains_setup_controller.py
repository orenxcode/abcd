from model.trains_setup_model import TrainsSetup


class TrainsSetupControlers:

    
    def create_table_trains_controller():
        reuslt=TrainsSetup.create_table_trains()
        return {"message":reuslt}
    

    def insert_trains_controller(name,engine,speed,route,type,line_id):
        result=TrainsSetup.insert_trains(name,engine,speed,route,type,line_id)
        return {"message":result}
    

    def create_table_lines_controller():
        reuslt=TrainsSetup.create_table_lines()
        return {"message":reuslt}
    

    def insert_lines_controller(name,status):
        result=TrainsSetup.insert_lines(name,status)
        return {"message":result}

