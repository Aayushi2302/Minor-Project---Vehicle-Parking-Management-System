from flask import jsonify
from typing import Optional

class ErrorResponse:
    success = False

    @staticmethod
    def jsonify_error(custom_error) -> dict:
        return  jsonify(
                    {
                        "success" : ErrorResponse.success,
                        "error" : custom_error.error,
                        "message" : custom_error.message
                    }
                )

class SuccessResponse:
    success = True

    @staticmethod
    def jsonify_data(message, data: Optional[dict] = {}) -> dict:
        return  jsonify(
                    {
                        "success" : SuccessResponse.success,
                        "message" : message,
                        "data" : data
                    }
                )