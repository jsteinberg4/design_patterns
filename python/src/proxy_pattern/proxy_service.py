import logging
from typing import Any, Optional

from python.src.proxy_pattern.abstract_service import AbstractService

LOG = logging.getLogger(__name__)


class ProxyService(AbstractService):
    """An implementation of the Proxy pattern.

    Represents an AbstractService which delegates any operations from
    `AbstractService` to a separate class, which actually implements the
    correct business logic. This intermediary layer allows for things like
    access control, delayed database connections, etc.
    """

    def __init__(self, service: Optional[AbstractService] = None) -> None:
        """
        Instantiate a new proxy object for `service`

        :param service:
        :type service:
        """
        super().__init__()
        self._proxied_service: Optional[AbstractService] = service

    @property
    def proxied_service(self):
        return self._proxied_service

    @proxied_service.setter
    def proxied_service(self, new_service: AbstractService) -> None:
        if issubclass(type(new_service), AbstractService):
            self._proxied_service = new_service
        else:
            raise ValueError(f"Proxied service must be a subclass of "
                             f"`AbstractService`. Received: {new_service}")

    def operation(self, *args, **kwargs) -> Any:
        LOG.info(f"Processing operation via proxy service: {str(self)}")
        op_result = self.proxied_service.operation(*args, **kwargs)
        LOG.info(f"Completed operation from proxy service")

        return op_result

    def __repr__(self) -> str:
        """Represent the name & properties of this class as a string"""
        return "{cls_name}(proxy={proxy_name})".format(
            cls_name=self.__class__.__name__,
            proxy_name=str(self.proxied_service),
        )
