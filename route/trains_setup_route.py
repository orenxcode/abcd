from flask import jsonify,request,Blueprint
from controller.trains_setup_controller import TrainsSetupControler


trainsSetupBP=Blueprint("trainsSetupBP",__name__)


@trainsSetupBP.route("/set/table/trains",methods=["POST"])
def create_table_trains_route():
    result=TrainsSetupControler.create_table_trains_controller()
    return jsonify (result)


@trainsSetupBP.route("/set/table/lines",methods=["POST"])
def create_table_lines_route():
    result=TrainsSetupControler.create_table_lines_controller()
    return jsonify (result)


@trainsSetupBP.route("/set/insert/trains",methods=["POST"])
def insert_trains_route():
    result=TrainsSetupControler.insert_trains_controller()
    return jsonify (result)


@trainsSetupBP.route("/set/insert/lines",methods=["POST"])
def insert_lines_route():
    result=TrainsSetupControler.insert_lines_controller()
    return jsonify (result)


