from abc import ABC, abstractmethod
from typing import Any


class AbstractService(ABC):
    """Abstract service for a proxy pattern"""

    @abstractmethod
    def operation(self, *args, **kwargs) -> Any:
        """A stub 'do-something' method for any service"""
        pass
