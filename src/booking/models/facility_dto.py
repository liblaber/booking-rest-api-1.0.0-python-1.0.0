# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class FacilityDtoAttributes(Enum):
    """An enumeration representing different categories.

    :cvar OFFSITE: "OFFSITE"
    :vartype OFFSITE: str
    :cvar PAID: "PAID"
    :vartype PAID: str
    """

    OFFSITE = "OFFSITE"
    PAID = "PAID"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, FacilityDtoAttributes._member_map_.values()))


@JsonMap({"id_": "id"})
class FacilityDto(BaseModel):
    """The list of facilities available in this property. Requires `{"extras":["facilities"]}`.

    :param id_: A signed integer number that uniquely identifies an accommodation property facility. Examples of facilities are: Parking, Restaurant, Room service etc. , defaults to None
    :type id_: int, optional
    :param attributes: List of optional attributes for this facility., defaults to None
    :type attributes: List[FacilityDtoAttributes], optional
    """

    def __init__(self, id_: int = None, attributes: List[FacilityDtoAttributes] = None):
        if id_ is not None:
            self.id_ = id_
        if attributes is not None:
            self.attributes = self._define_list(attributes, FacilityDtoAttributes)