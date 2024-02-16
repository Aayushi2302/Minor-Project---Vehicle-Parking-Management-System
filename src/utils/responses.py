"""Module containing response format for success and error."""

from flask import jsonify, Response


class ErrorResponse:
    """Class for error response format."""
    success = False

    @staticmethod
    def jsonify_error(custom_error) -> Response:
        return jsonify(
            {
                "success": ErrorResponse.success,
                "error": custom_error.error,
                "message": custom_error.message
            }
        )


class SuccessResponse:
    """Class for success response format."""
    success = True

    @staticmethod
    def jsonify_data(message, data: list = []) -> Response:
        return jsonify(
            {
                "success": SuccessResponse.success,
                "message": message,
                "data": data
            }
        )
