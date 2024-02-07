"""Module containing logic related to authorization tokens."""
from mysql import connector
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                get_jwt,
                                get_jti)

from src.config.query import QueryConfig
from src.business.token_business.token_access import TokenAccess
from src.models.database import Database
from src.utils.custom_exceptions import DBException

class AuthTokenBusiness(TokenAccess):
    """
        Class containing logic related creating and handling authorization tokens.
        ...
        Methods
        -------
        create_token(): tuple -> This method will be responsible for creating tokens.
        get_user_claims(): str -> This method will be responsible for getting user related claims.
        revoke_token(): None -> This method will be responsible for revoking access and refresh tokens.
    """
    def __init__(self, db: Database) -> None:
        """Constructor for auth token business."""
        self.db = db

    def create_token(self,
        fresh_token: bool,
        user_identity: str,
        user_additional_claim: dict
    ) -> tuple :
        """
            Method responsible for generating tokens.
            Parameter -> fresh_token: bool, user_identity: str, user_additional_claim: dict
            Return type -> tuple
        """
        self.revoke_token(user_identity)
        access_token =  create_access_token(
                            identity = user_identity,
                            fresh = fresh_token,
                            additional_claims = user_additional_claim
                        )
        access_token_jti = get_jti(access_token)

        refresh_token = create_refresh_token(
                            identity = user_identity,
                            additional_claims = user_additional_claim
                        )
        refresh_token_jti = get_jti(refresh_token)

        self.save_tokens_to_database(user_identity, access_token_jti, refresh_token_jti)
        return (access_token, refresh_token)

    def get_user_claims(self) -> dict:
        """
            Method to get user claims.
            Parameter -> None
            Return type -> str
        """
        return get_jwt()

    def save_tokens_to_database(self,
                                user_identity: str,
                                access_token: str,
                                refresh_token: str
    ) -> None:
        """
            Method to save tokens generated to database.
            Parameter -> access_token: str, refresh_token: str
            Return type -> None
        """
        try:
            self.db.save_data_to_database(
                QueryConfig.CREATE_TOKEN,
                (user_identity, access_token, refresh_token)
            )
        except connector.Error as error:
            print(error)
            raise DBException(500, "Internal Server Error", "Something wrong with the server.")

    def revoke_token(self, user_identity: str) -> None:
        """
            Method responsible for revoking access and refresh tokens.
            Parameter -> access_token: str
            Return type -> None
        """
        self.db.save_data_to_database(
            QueryConfig.REVOKE_TOKEN,
            (user_identity, )
        )
