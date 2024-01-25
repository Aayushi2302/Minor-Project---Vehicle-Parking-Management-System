from abc import ABC, abstractmethod
from typing import Optional

class AuthorizationToken(ABC):

    @abstractmethod
    def create_token(self,
        fresh_token: bool,
        user_identity: str,
        user_additional_claim: Optional[dict] = None
    ) -> None:
        ...

    @abstractmethod
    def get_user_identity(self) -> None:
        ...
        