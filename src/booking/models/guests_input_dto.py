# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .allocation_input_dto import AllocationInputDto


@JsonMap({})
class GuestsInputDto(BaseModel):
    """The guest details for the request.

    :param number_of_adults: The number of adults for the search.
    :type number_of_adults: int
    :param number_of_rooms: The number of rooms needed.
    :type number_of_rooms: int
    :param allocation: The exact allocation of guests to rooms., defaults to None
    :type allocation: List[AllocationInputDto], optional
    :param children: Array with the children ages., defaults to None
    :type children: List[int], optional
    """

    def __init__(
        self,
        number_of_adults: int,
        number_of_rooms: int,
        allocation: List[AllocationInputDto] = None,
        children: List[int] = None,
    ):
        self.number_of_adults = number_of_adults
        self.number_of_rooms = number_of_rooms
        if allocation is not None:
            self.allocation = self._define_list(allocation, AllocationInputDto)
        if children is not None:
            self.children = children
