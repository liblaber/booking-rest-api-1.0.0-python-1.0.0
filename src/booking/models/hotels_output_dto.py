# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .hotel_data_dto import HotelDataDto
from .room_data_dto import RoomDataDto


@JsonMap({})
class HotelsOutputDto(BaseModel):
    """HotelsOutputDto

    :param hotel_data: Hotel specific information., defaults to None
    :type hotel_data: HotelDataDto, optional
    :param hotel_id: Unique ID to represent this hotel., defaults to None
    :type hotel_id: int, optional
    :param room_data: This block has room data for this hotel., defaults to None
    :type room_data: List[RoomDataDto], optional
    """

    def __init__(
        self,
        hotel_data: HotelDataDto = None,
        hotel_id: int = None,
        room_data: List[RoomDataDto] = None,
    ):
        if hotel_data is not None:
            self.hotel_data = self._define_object(hotel_data, HotelDataDto)
        if hotel_id is not None:
            self.hotel_id = hotel_id
        if room_data is not None:
            self.room_data = self._define_list(room_data, RoomDataDto)