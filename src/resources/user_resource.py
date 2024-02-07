"""Module having end points related to user."""from flask_jwt_extended import jwt_requiredfrom flask_smorest import Blueprintfrom flask.views import MethodViewfrom schemas.user_schema import (UserProfileSchema,                                 ChangePasswordRequestSchema,                                 ChangePasswordResponseSchema)from config.app_config import AppConfigfrom business.token_business.auth_token_business import AuthTokenBusinessfrom controller.user_controller.user_profile_controller import UserProfileControllerfrom controller.user_controller.change_password_controller import ChangePasswordControllerfrom models.database import dbfrom utils.rbac import role_based_accessfrom utils.role_mapping import RoleMappingblp = Blueprint("user", __name__, description = "User related operations")@blp.route("/v1/my-profile")class UserProfile(MethodView):    """        Class containing various methods applicable to /v1/my-profile route.        ...        Methods        -------        GET    """    @blp.doc(parameters = [AppConfig.BLP_DOC_PARAMETERS])    @blp.response(200, UserProfileSchema)    @role_based_access((RoleMapping["admin"], RoleMapping["attendant"]))    def get(self) -> dict:        """            Method for fetching user profile who is loggedin.            ...            On Success -> Follows UserProfileSchema and returns user related information.            On Failure -> Returns success = False and error message.        """        token_obj = AuthTokenBusiness(db)        username = token_obj.get_user_claims()["sub"]        role = token_obj.get_user_claims()["usr"]        return UserProfileController().get_user_profile_data(username, role)@blp.route("/v1/change-password")class ChangeUserPassword(MethodView):    """        Class containing various methods applicable to /v1/change-password route.        ...        Methods        -------        PUT    """    @blp.doc(parameters = [AppConfig.BLP_DOC_PARAMETERS])    @blp.arguments(ChangePasswordRequestSchema)    @blp.response(200, ChangePasswordResponseSchema)    @jwt_required()    def put(self, user_data):        """            Method for changing user password on first login.            ...            On Success -> Follows ChangePasswordResponseSchema and returns new access and refresh tokens.            On Failure -> Returns success = False and error message.        """        token_obj = AuthTokenBusiness(db)        username = token_obj.get_user_claims()["sub"]        role = token_obj.get_user_claims()["usr"]        return ChangePasswordController().change_user_password(user_data, username, role)