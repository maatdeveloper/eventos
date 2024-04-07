from flask import Blueprint, jsonify, request
from src.http_types.http_request import HTTPRequest
from src.data.event_handler import EventHandler

event_route_bp = Blueprint("event_route", __name__)

@event_route_bp.route("/events", methods=["POST"])
def create_event():
    http_request = HTTPRequest(body=request.json)
    event_handler = EventHandler()
    
    http_response = event_handler.register(http_request)
    return jsonify({"ola": "mundo"}), http_response.status_code

