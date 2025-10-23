from abc import ABC
from typing import Any, Dict


class DomainException(Exception, ABC):
    error_code: str = "domain_error"  # estable y log-friendly
    status_code: int = 400  # por defecto; no acoples a HTTP si no quieres
    message: str = "Domain error"

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or self.message)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "error": self.error_code,
            "message": self.message,
        }
