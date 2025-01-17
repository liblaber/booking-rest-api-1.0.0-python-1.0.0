# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class ProgramSettingsDto(BaseModel):
    """Details of programmes undergone by the property.

    :param travel_proud: Boolean value is "true" if property has travel proud badge and "false" otherwise., defaults to None
    :type travel_proud: bool, optional
    """

    def __init__(self, travel_proud: bool = None):
        if travel_proud is not None:
            self.travel_proud = travel_proud
