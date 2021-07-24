import logging
from typing import Any

from python.src.proxy_pattern.abstract_service import AbstractService

LOG = logging.getLogger(__name__)


class DatabaseService(AbstractService):
    def __init__(self) -> None:
        super().__init__()

    def operation(self, *args, **kwargs) -> Any:
        LOG.info(f"{self.__class__.__name__}: Connecting to database "
                 f"directly...")
        # TODO :: some sort of business logic here (i.e. connect to a DB)
        LOG.info("Finished database operation")

        return True

    def __repr__(self) -> str:
        return "{cls_name}()".format(
            cls_name=self.__class__.__name__,
        )
