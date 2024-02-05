"""Module containing abstract class responsible for generating and handling tokens."""

from abc import ABC, abstractmethod

class TokenAccess(ABC):
    """
        Abstract class having abstract methods related to creating and handling tokens.
        ...
        Methods
        -------
        create_token() : tuple -> This method will be responsible for creating tokens.
        get_user_claims() : str -> This method will be responsible for getting user related claims.
    """
    @abstractmethod
    def create_token(self,
        fresh_token: bool,
        user_identity: str,
        user_additional_claim: dict
    ) -> tuple:
        """Method that will be responsible for creating tokens."""

    @abstractmethod
    def get_user_claims(self) -> str:
        """Method that will be responsible for getting user related claims."""

    @abstractmethod
    def revoke_token(self, user_identity: str) -> None:
        """Method that will be responsible for revoking access and refresh tokens."""
        