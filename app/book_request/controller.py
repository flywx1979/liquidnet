from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import BookRequestSchema
from .service import BookRequestService
from .model import BookRequest
from .contract import BookRequestContract
from .validator import Validator
from flask import jsonify

api = Namespace("book_request", description="Book Request Namespace Registry")


@api.route("/request")
class BookRequestResource(Resource):

    @accepts(schema=BookRequestSchema, api=api)
    def post(self) -> Response:
        if Validator.validate(request.parsed_obj):
           return jsonify(dict(status="success", data=BookRequestService.create(request.parsed_obj)))
        return jsonify(error=400, text=message.Errors["400_MESSAGE"])


@api.route("/<int:requestId>")
@api.param("requestId", "User book request ID")

    def get(self, requestId: int) -> Response:
        if not request_id:
           return jsonify(dict(status="success", data=BookRequestService.get_all()))
        else:
           return jsonify(dict(status="success", data=BookRequestService.get_by_id(requestId)))
        return jsonify(error=400, text=message.Errors["400_MESSAGE"])

    def delete(self, requestId: int) -> Response:
        if requestId:
            return  return jsonify(dict(status="success", data=BookRequestService.delete_by_id(requestId)))
        else:
            return jsonify(error=400, text=message.Errors["400_MESSAGE"])
