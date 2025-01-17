# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .translation_dto import TranslationDto


@JsonMap({})
class HotelFacilityTypeOutputDto(BaseModel):
    """HotelFacilityTypeOutputDto

    :param hotel_facility_type_id: Unique ID of the hotel facility type., defaults to None
    :type hotel_facility_type_id: int, optional
    :param facility_type_id: The type of facility this is, mapped from FacilityTypes., defaults to None
    :type facility_type_id: int, optional
    :param name: The name of this facility type in english., defaults to None
    :type name: str, optional
    :param translations: The fields and their translations in various languages. They are only shown if we have the translations available., defaults to None
    :type translations: List[TranslationDto], optional
    """

    def __init__(
        self,
        hotel_facility_type_id: int = None,
        facility_type_id: int = None,
        name: str = None,
        translations: List[TranslationDto] = None,
    ):
        if hotel_facility_type_id is not None:
            self.hotel_facility_type_id = hotel_facility_type_id
        if facility_type_id is not None:
            self.facility_type_id = facility_type_id
        if name is not None:
            self.name = name
        if translations is not None:
            self.translations = self._define_list(translations, TranslationDto)
