"""
    Module containing business logic related to the creation of new access token(fresh=False)
    and refresh token.
"""

import pymysql

from src.business.token_business.token_access import TokenAccess
from src.config.app_config import AppConfig
from src.config.query import QueryConfig
from src.models.database import Database
from src.utils.custom_exceptions import AppException, DBException


class RefreshTokenBusiness:
    """
        Class containing business logic related to access and refresh token generation.
        ...
        Attributes
        ----------
        db: Database Object
        token: TokenAccess Object
    """
    def __init__(self, db: Database, token: TokenAccess) -> None:
        """Constructor for refresh token business."""
        self.db = db
        self.token = token

    def generate_new_token(self, refresh_jti: str, user_identity: str, role: str, p_type: int) -> list:
        """
            Method to generate new access and refresh tokens.
            Parameters -> refresh_jti: str, user_identity: str, role: str, p_type: int
            Returns -> list
        """
        try:
            data = self.db.fetch_data_from_database(
                                QueryConfig.FETCH_REFRESH_TOKEN,
                            (user_identity, AppConfig.TOKEN_ISSUED)
                            )
            if not data:
                raise AppException(401, "Unauthorized", "No active token. Please login again.")

            get_token_jti = data[0]["refresh_token"]

            if refresh_jti != get_token_jti:
                raise AppException(401, "Unauthorized", "Invalid token. Provide a valid token.")

            self.token.revoke_token(user_identity)
            tokens = self.token.create_token(False, user_identity,
                                             {"usr": role, "pty": p_type})
            access_token = tokens[0]
            refresh_token = tokens[1]
            return [{
                "access_token": access_token,
                "refresh_token": refresh_token
            }]
        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "Something wrong with the server.")

