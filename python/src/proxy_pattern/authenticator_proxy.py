import logging
from typing import Any, Dict, Optional

from python.src.proxy_pattern.abstract_service import AbstractService
from python.src.proxy_pattern.proxy_service import ProxyService

LOG = logging.getLogger(__name__)


class AuthenticatorProxyService(ProxyService):
    """A proxy object which implements access control.

    Requires valid credentials in order to pass work to the real service.
    """

    def __init__(self, service: Optional[AbstractService] = None,
                 credential_map: Dict[str, bool] = {}) -> None:
        super().__init__(service)
        self._credentials = credential_map

    def set_credential(self, user: str, can_access: bool) -> None:
        """Adds a user to the access control list.

        NOTE :: Method is destructive. This will overwrite any existing
        access settings for the given user.

        :param user: username to set access for
        :param can_access: T/F whether `user` will be allowed to access the
                           proxied service
        """
        LOG.info(f"Updating access control: user={user}, "
                 f"can_access={can_access}")
        self._credentials.update({user: can_access})

    def operation(self, user: str = None, *args, **kwargs) -> Any:
        LOG.info(f"Checking if user can access service before "
                 f"handing off request")
        result = None

        if user is None or not self._credentials.get(user, False):
            LOG.info(f"User ({user}) cannot access the current service "
                     f"({self.proxied_service}). Rejecting request.")
        else:
            LOG.info(f"User ({user}) has access to the proxied service "
                     f"({self.proxied_service}). Handing off request.")
            result = self.proxied_service.operation(*args, **kwargs)

        return result
