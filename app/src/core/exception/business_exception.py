from typing import Any
from fastapi import HTTPException

class BusinessException(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: Any = None,
    ) -> None:
        super().__init__(status_code=status_code, detail=detail)
