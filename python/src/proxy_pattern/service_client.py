import logging

from python.src.proxy_pattern.abstract_service import AbstractService
from python.src.proxy_pattern.authenticator_proxy import \
    AuthenticatorProxyService
from python.src.proxy_pattern.database_service import DatabaseService
from python.src.proxy_pattern.proxy_service import ProxyService

LOG = logging.getLogger(__name__)


if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    LOG.info("Doing an operation without a proxy....")
    service: AbstractService = DatabaseService()
    res = service.operation()

    LOG.info("--------------------------")

    LOG.info("Doing an operation with a proxy....")
    proxy: AbstractService = ProxyService()
    proxy.proxied_service = DatabaseService()
    res = proxy.operation()

    LOG.info("--------------------------")

    LOG.info("Doing an operation with an authenticated proxy..")
    auth_proxy: AbstractService = AuthenticatorProxyService()
    auth_proxy.proxied_service = DatabaseService()

    # Try without valid credentials first
    res = auth_proxy.operation(user="jesse")
    auth_proxy.set_credential(user="jesse", can_access=True)
    res = auth_proxy.operation(user="jesse")

    print("Done")