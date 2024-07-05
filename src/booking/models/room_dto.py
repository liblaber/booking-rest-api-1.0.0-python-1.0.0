# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .translated_string import TranslatedString
from .bed_option_dto import BedOptionDto
from .cribs_and_extra_beds_dto import CribsAndExtraBedsDto
from .room_maximum_occupancy_dto import RoomMaximumOccupancyDto
from .number_of_rooms_dto import NumberOfRoomsDto


class RoomDtoAttributes(Enum):
    """An enumeration representing different categories.

    :cvar NON_SMOKING: "NON_SMOKING"
    :vartype NON_SMOKING: str
    :cvar WORK_FRIENDLY: "WORK_FRIENDLY"
    :vartype WORK_FRIENDLY: str
    """

    NON_SMOKING = "NON_SMOKING"
    WORK_FRIENDLY = "WORK_FRIENDLY"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, RoomDtoAttributes._member_map_.values()))


@JsonMap({"id_": "id"})
class RoomDto(BaseModel):
    """The list of room types available at this property. Requires `{"extras":["rooms"]}`.

    :param id_: A signed integer number that uniquely identifies an accommodation property room., defaults to None
    :type id_: int, optional
    :param name: Translated description of this room. The maximum number of characters returned may be limited by contract., defaults to None
    :type name: TranslatedString, optional
    :param attributes: Lists a set of attribute qualifiers for this room. Will not be returned if no relevant attributes are applicable., defaults to None
    :type attributes: List[RoomDtoAttributes], optional
    :param bed_options: Lists all possible bedding options for this room or apartment., defaults to None
    :type bed_options: List[BedOptionDto], optional
    :param cribs_and_extra_beds: Lists room options regarding adding cribs and/or extra beds., defaults to None
    :type cribs_and_extra_beds: CribsAndExtraBedsDto, optional
    :param description: Translated description of this room. The maximum number of characters returned may be limited by contract., defaults to None
    :type description: TranslatedString, optional
    :param facilities: A signed integer number that uniquely identifies an accommodation property room facility. Examples of facilities are: Coffee/Tea maker, TV, Airconditioning, etc., defaults to None
    :type facilities: List[int], optional
    :param maximum_occupancy: Occupancy limits and options., defaults to None
    :type maximum_occupancy: RoomMaximumOccupancyDto, optional
    :param number_of_rooms: Total rooms available., defaults to None
    :type number_of_rooms: NumberOfRoomsDto, optional
    :param room_type: A signed integer number that uniquely identifies an accommodation property room type. Example of room types are: Suite, Apartment, Twin/Double etc. , defaults to None
    :type room_type: int, optional
    :param size: The room area in square meters., defaults to None
    :type size: int, optional
    """

    def __init__(
        self,
        id_: int = None,
        name: TranslatedString = None,
        attributes: List[RoomDtoAttributes] = None,
        bed_options: List[BedOptionDto] = None,
        cribs_and_extra_beds: CribsAndExtraBedsDto = None,
        description: TranslatedString = None,
        facilities: List[int] = None,
        maximum_occupancy: RoomMaximumOccupancyDto = None,
        number_of_rooms: NumberOfRoomsDto = None,
        room_type: int = None,
        size: int = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = self._define_object(name, TranslatedString)
        if attributes is not None:
            self.attributes = self._define_list(attributes, RoomDtoAttributes)
        if bed_options is not None:
            self.bed_options = self._define_list(bed_options, BedOptionDto)
        if cribs_and_extra_beds is not None:
            self.cribs_and_extra_beds = self._define_object(
                cribs_and_extra_beds, CribsAndExtraBedsDto
            )
        if description is not None:
            self.description = self._define_object(description, TranslatedString)
        if facilities is not None:
            self.facilities = facilities
        if maximum_occupancy is not None:
            self.maximum_occupancy = self._define_object(
                maximum_occupancy, RoomMaximumOccupancyDto
            )
        if number_of_rooms is not None:
            self.number_of_rooms = self._define_object(
                number_of_rooms, NumberOfRoomsDto
            )
        if room_type is not None:
            self.room_type = room_type
        if size is not None:
            self.size = size