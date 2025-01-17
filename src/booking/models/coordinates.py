# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class Coordinates(BaseModel):
    """Limit the result list to the specified coordinates.

    :param latitude: Specify a latitude (as well as a longitude and radius) to do searches around a specific location.
    :type latitude: float
    :param longitude: Specify a longitude (as well as a latitude and radius) to do searches around a specific location.
    :type longitude: float
    :param radius: The radius is km to search around the specified latitude and longitude.
    :type radius: float
    """

    def __init__(self, latitude: float, longitude: float, radius: float):
        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius
