from loguru import logger

__all__ = ["BaseAppException"]


class BaseAppException(Exception):
    def __init__(self, message: str = "") -> None:
        super().__init__(message)
        self.message = message
        logger.trace("Exception '{}' was raised. {}.", self.__class__.__name__, self.message)

    @property
    def error_code(self) -> int:
        raise NotImplementedError("Error code should be implemented.")

    def to_dict(self) -> dict:
        raise NotImplementedError("`to_dict` is not implemented.")
