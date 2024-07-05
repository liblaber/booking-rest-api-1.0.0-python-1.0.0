# This file was generated by liblab | https://liblab.com/

from .services.demand_api_v3_compatible import DemandApiV3CompatibleService
from .services.demand_api_v2_compatible import DemandApiV2CompatibleService
from .net.environment import Environment


class Booking:
    def __init__(
        self,
        access_token: str = None,
        api_key: str = None,
        api_key_header: str = "X-Affiliate-id",
        base_url: str = Environment.DEFAULT.value,
    ):
        """
        Initializes Booking the SDK class.
        """
        self.demand_api_v3_compatible = DemandApiV3CompatibleService(base_url=base_url)
        self.demand_api_v2_compatible = DemandApiV2CompatibleService(base_url=base_url)
        self.set_access_token(access_token)
        self.set_api_key(api_key, api_key_header)

    def set_base_url(self, base_url):
        """
        Sets the base URL for the entire SDK.
        """
        self.demand_api_v3_compatible.set_base_url(base_url)
        self.demand_api_v2_compatible.set_base_url(base_url)

        return self

    def set_access_token(self, access_token: str):
        """
        Sets the access token for the entire SDK.
        """
        self.demand_api_v3_compatible.set_access_token(access_token)
        self.demand_api_v2_compatible.set_access_token(access_token)

        return self

    def set_api_key(self, api_key: str, api_key_header="X-Affiliate-id"):
        """
        Sets the api key and the api key header for the entire SDK.
        """
        self.demand_api_v3_compatible.set_api_key(api_key, api_key_header)
        self.demand_api_v2_compatible.set_api_key(api_key, api_key_header)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c