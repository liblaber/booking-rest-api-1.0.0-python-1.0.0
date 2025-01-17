# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .alternative_key_location_dto import AlternativeKeyLocationDto


@JsonMap({})
class KeyCollectionInformationDto(BaseModel):
    """KeyCollectionInformationDto

    :param alternate_location: Alternate location to collect the key of this accommodation property. This is returned if the key to access the property is in another location. , defaults to None
    :type alternate_location: AlternativeKeyLocationDto, optional
    :param checkin_method: An enumeration that describes the conditions for the checkin process and for collecting the key to access the property. This is typically relevant for non-hotel accommodations (like houses or apartments) without a 24 hours front-desk. , defaults to None
    :type checkin_method: str, optional
    :param key_location: Location of the key to access this accommodation property., defaults to None
    :type key_location: str, optional
    """

    def __init__(
        self,
        alternate_location: AlternativeKeyLocationDto = None,
        checkin_method: str = None,
        key_location: str = None,
    ):
        if alternate_location is not None:
            self.alternate_location = self._define_object(
                alternate_location, AlternativeKeyLocationDto
            )
        if checkin_method is not None:
            self.checkin_method = checkin_method
        if key_location is not None:
            self.key_location = key_location
