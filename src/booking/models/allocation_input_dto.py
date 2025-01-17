# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class AllocationInputDto(BaseModel):
    """The exact allocation of guests to rooms.

    :param children: The children ages for this room., defaults to None
    :type children: List[int], optional
    :param number_of_adults: The number of adults for this room.
    :type number_of_adults: int
    """

    def __init__(self, number_of_adults: int, children: List[int] = None):
        if children is not None:
            self.children = children
        self.number_of_adults = number_of_adults
