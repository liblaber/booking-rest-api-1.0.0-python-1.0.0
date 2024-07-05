# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class Tags(Enum):
    """An enumeration representing different categories.

    :cvar BLACK_FRIDAY: "BLACK_FRIDAY"
    :vartype BLACK_FRIDAY: str
    :cvar GENIUS: "GENIUS"
    :vartype GENIUS: str
    :cvar LIMITED_TIME_DEAL: "LIMITED_TIME_DEAL"
    :vartype LIMITED_TIME_DEAL: str
    :cvar LOGGED_IN_DEAL: "LOGGED_IN_DEAL"
    :vartype LOGGED_IN_DEAL: str
    :cvar MOBILE_RATE: "MOBILE_RATE"
    :vartype MOBILE_RATE: str
    :cvar SEASONAL_DEAL: "SEASONAL_DEAL"
    :vartype SEASONAL_DEAL: str
    """

    BLACK_FRIDAY = "BLACK_FRIDAY"
    GENIUS = "GENIUS"
    LIMITED_TIME_DEAL = "LIMITED_TIME_DEAL"
    LOGGED_IN_DEAL = "LOGGED_IN_DEAL"
    MOBILE_RATE = "MOBILE_RATE"
    SEASONAL_DEAL = "SEASONAL_DEAL"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Tags._member_map_.values()))


@JsonMap({})
class DealDto(BaseModel):
    """This specifies the deal tagging for the product.

    :param discount_percentage: discount_percentage, defaults to None
    :type discount_percentage: int, optional
    :param public_price: public_price, defaults to None
    :type public_price: float, optional
    :param tags: tags, defaults to None
    :type tags: List[Tags], optional
    """

    def __init__(
        self,
        discount_percentage: int = None,
        public_price: float = None,
        tags: List[Tags] = None,
    ):
        if discount_percentage is not None:
            self.discount_percentage = discount_percentage
        if public_price is not None:
            self.public_price = public_price
        if tags is not None:
            self.tags = self._define_list(tags, Tags)