from http import HTTPStatus
from flask import Blueprint, Response, make_response

err_handler_bp = Blueprint('errors', __name__)

@err_handler_bp.app_errorhandler(HTTPStatus.NOT_FOUND)
def handle_404(error: int) -> Response:
    return make_response("Об'єкт не знайдено", HTTPStatus.NOT_FOUND)

@err_handler_bp.app_errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
def handle_422(error: int) -> Response:
    return make_response("Введені дані некоректні або неповні", HTTPStatus.UNPROCESSABLE_ENTITY)

@err_handler_bp.app_errorhandler(HTTPStatus.CONFLICT)
def handle_409(error: int) -> Response:
    return make_response("Такий об'єкт вже існує в БД", HTTPStatus.CONFLICT)

@err_handler_bp.app_errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def handle_500(error: int) -> Response:
    return make_response("Сталася внутрішня помилка сервера", HTTPStatus.INTERNAL_SERVER_ERROR)

@err_handler_bp.app_errorhandler(Exception)
def handle_exception(error: Exception) -> Response:
    return make_response("Сталася помилка: {}".format(str(error)), HTTPStatus.INTERNAL_SERVER_ERROR)
