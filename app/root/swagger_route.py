from flask import Blueprint, jsonify, request, current_app
from flask_swagger_ui import get_swaggerui_blueprint

swagger_bp = Blueprint("swagger_bp", __name__)

SWAGGER_URL = "/swagger"
API_URL = "/swagger.json"

swagger_ui_bp = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Gym API"}
)

EXCLUDE_ENDPOINTS = {"static", "swagger_bp.swagger_json"}
METHODS_ALLOWED = {"GET", "POST", "PUT", "PATCH", "DELETE"}

def _path_item_for_methods(methods):
    obj = {}
    for m in sorted(methods):
        obj[m.lower()] = {
            "summary": f"{m} request",
            "parameters": [],
            "responses": {
                "200": {"description": "OK"},
                "201": {"description": "Created"},
                "204": {"description": "No Content"},
                "400": {"description": "Bad Request"},
                "404": {"description": "Not Found"},
                "500": {"description": "Server Error"}
            }
        }
    return obj

def _should_exclude(rule):
    if rule.endpoint in EXCLUDE_ENDPOINTS:
        return True
    methods = METHODS_ALLOWED.intersection(rule.methods or set())
    return len(methods) == 0

@swagger_bp.route("/swagger.json")
def swagger_json():
    host = request.host
    scheme = request.scheme if request.scheme in ("http", "https") else "http"

    paths = {}
    for rule in current_app.url_map.iter_rules():
        if _should_exclude(rule):
            continue
        path = str(rule.rule).replace("<", "{").replace(">", "}")
        methods = METHODS_ALLOWED.intersection(rule.methods or set())
        paths.setdefault(path, {}).update(_path_item_for_methods(methods))

    spec = {
        "swagger": "2.0",
        "info": {"title": "Gym API", "version": "1.0.0"},
        "host": host,
        "basePath": "/",
        "schemes": [scheme],
        "paths": paths,
    }
    return jsonify(spec)
