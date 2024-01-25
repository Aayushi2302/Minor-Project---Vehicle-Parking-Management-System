from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, get_jwt
from typing import Optional
from tokens.authorization_token import AuthorizationToken

class Token(AuthorizationToken):

    def create_token(self,
        fresh_token: bool,
        user_identity: str,
        user_additional_claim: Optional[dict] = None
    ) -> tuple :
        access_token =  create_access_token(
                            identity = user_identity,
                            fresh = fresh_token,
                            additional_claims = user_additional_claim
                        )

        refresh_token = create_refresh_token(
                            identity = user_identity,
                            additional_claims = user_additional_claim
                        )

        return (access_token, refresh_token)

    def get_user_identity(self) -> str:
        return get_jwt_identity()