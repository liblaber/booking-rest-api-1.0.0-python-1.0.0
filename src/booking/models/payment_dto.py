# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class PaymentTypes(Enum):
    """An enumeration representing different categories.

    :cvar PAY_LATER: "PAY_LATER"
    :vartype PAY_LATER: str
    :cvar PAY_NOW: "PAY_NOW"
    :vartype PAY_NOW: str
    """

    PAY_LATER = "PAY_LATER"
    PAY_NOW = "PAY_NOW"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, PaymentTypes._member_map_.values()))


@JsonMap({})
class PaymentDto(BaseModel):
    """Payment terms and conditions for this product.

    :param payment_types: payment_types, defaults to None
    :type payment_types: List[PaymentTypes], optional
    """

    def __init__(self, payment_types: List[PaymentTypes] = None):
        if payment_types is not None:
            self.payment_types = self._define_list(payment_types, PaymentTypes)