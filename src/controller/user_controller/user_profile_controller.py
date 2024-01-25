from models.database import db
from business.user_business import UserBusiness
from utils.responses import SuccessResponse
from utils.custom_error_handler import custom_error_handler
from tokens.authorization_token import AuthorizationToken

class UserProfileController:

    def __init__(self, token_obj: AuthorizationToken) -> None:
        self.token_obj = token_obj

    @custom_error_handler
    def get_user_profile_data(self) -> dict:
        username = self.token_obj.get_user_identity()
        user_business_obj = UserBusiness(db)
        data = user_business_obj.get_user_details(username)
        return SuccessResponse.jsonify_data("Data fetched successfully.", data), 200
