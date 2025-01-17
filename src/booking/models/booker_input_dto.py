# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class Platform(Enum):
    """An enumeration representing different categories.

    :cvar ANDROID: "ANDROID"
    :vartype ANDROID: str
    :cvar DESKTOP: "DESKTOP"
    :vartype DESKTOP: str
    :cvar IOS: "IOS"
    :vartype IOS: str
    :cvar MOBILE: "MOBILE"
    :vartype MOBILE: str
    :cvar TABLET: "TABLET"
    :vartype TABLET: str
    """

    ANDROID = "ANDROID"
    DESKTOP = "DESKTOP"
    IOS = "IOS"
    MOBILE = "MOBILE"
    TABLET = "TABLET"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Platform._member_map_.values()))


class TravelPurpose(Enum):
    """An enumeration representing different categories.

    :cvar BUSINESS: "BUSINESS"
    :vartype BUSINESS: str
    :cvar LEISURE: "LEISURE"
    :vartype LEISURE: str
    """

    BUSINESS = "BUSINESS"
    LEISURE = "LEISURE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, TravelPurpose._member_map_.values()))


class UserGroups(Enum):
    """An enumeration representing different categories.

    :cvar AUTHENTICATED: "AUTHENTICATED"
    :vartype AUTHENTICATED: str
    :cvar GENIUS: "GENIUS"
    :vartype GENIUS: str
    :cvar GENIUS2: "GENIUS2"
    :vartype GENIUS2: str
    :cvar GENIUS3: "GENIUS3"
    :vartype GENIUS3: str
    """

    AUTHENTICATED = "AUTHENTICATED"
    GENIUS = "GENIUS"
    GENIUS2 = "GENIUS2"
    GENIUS3 = "GENIUS3"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, UserGroups._member_map_.values()))


@JsonMap({})
class BookerInputDto(BaseModel):
    """The booker's information.

    :param country: The booker country for showing the best price for that user and obeying laws regarding the display of taxes and fees.
    :type country: str
    :param platform: The booker platform for showing the platform based deals and prices.
    :type platform: Platform
    :param travel_purpose: The travel purpose of the booker., defaults to None
    :type travel_purpose: TravelPurpose, optional
    :param user_groups: The user groups that the booker is a member of., defaults to None
    :type user_groups: List[UserGroups], optional
    """

    def __init__(
        self,
        country: str,
        platform: Platform,
        travel_purpose: TravelPurpose = None,
        user_groups: List[UserGroups] = None,
    ):
        self.country = self._pattern_matching(country, "^[a-z]{2}$", "country")
        self.platform = self._enum_matching(platform, Platform.list(), "platform")
        if travel_purpose is not None:
            self.travel_purpose = self._enum_matching(
                travel_purpose, TravelPurpose.list(), "travel_purpose"
            )
        if user_groups is not None:
            self.user_groups = self._define_list(user_groups, UserGroups)
