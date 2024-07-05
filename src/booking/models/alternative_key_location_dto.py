# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class AlternativeKeyLocationDto(BaseModel):
    """Alternate location to collect the key of this accommodation property.
    This is returned if the key to access the property is in another location.


    :param address: address, defaults to None
    :type address: dict, optional
    :param city: city, defaults to None
    :type city: dict, optional
    :param postal_code: postal_code, defaults to None
    :type postal_code: str, optional
    """

    def __init__(
        self, address: dict = None, city: dict = None, postal_code: str = None
    ):
        if address is not None:
            self.address = address
        if city is not None:
            self.city = city
        if postal_code is not None:
            self.postal_code = postal_code
