from flask import jsonify,request,Blueprint
from controller.trains_controller import TrainsController


trainsBP=Blueprint("trainsBP",__name__)

@trainsBP.route("/all/trains",methods=["GET"])
def get_all_trains_route():
    result=TrainsController.get_all_trains_controller()
    return jsonify (result)


@trainsBP.route("/all/lines",methods=["GET"])
def get_all_lines_route():
    result=TrainsController.get_all_lines_controller()
    return jsonify (result)


@trainsBP.route("/one/trains/<id>",methods=["GET"])
def get_one_by_id_trains_route(id):
    result=TrainsController.get_one_by_id_trains_controller(id)
    return jsonify (result)


@trainsBP.route("/update/trains/<id>",methods=["PATCH"])
def update_speed_by_id_trains_route(id):
    data=request.get_json()
    speed=data["speed"]
    result=TrainsController.update_speed_by_id_trains_controller(id,speed)
    return jsonify (result)


@trainsBP.route("/delete/trains/<id>",methods=["DELETE"])
def delete_by_id_trains_route(id):
    result=TrainsController.delete_by_id_trains_controller(id)
    return jsonify (result)


@trainsBP.route("/TLS",methods=["GET"])
def get_trains_lines_status_route():
    result=TrainsController.get_trains_lines_status_controller()
    return jsonify (result)


@trainsBP.route("/active",methods=["GET"])
def get_trains_lines_active_route():
    result=TrainsController.get_trains_lines_active_controller()
    return jsonify (result)

