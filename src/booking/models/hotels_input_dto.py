# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class HotelsInputDtoLanguage(Enum):
    """An enumeration representing different categories.

    :cvar AR: "AR"
    :vartype AR: str
    :cvar BG: "BG"
    :vartype BG: str
    :cvar CA: "CA"
    :vartype CA: str
    :cvar CS: "CS"
    :vartype CS: str
    :cvar DA: "DA"
    :vartype DA: str
    :cvar DE: "DE"
    :vartype DE: str
    :cvar EL: "EL"
    :vartype EL: str
    :cvar EN: "EN"
    :vartype EN: str
    :cvar EN_GB: "EN_GB"
    :vartype EN_GB: str
    :cvar EN_US: "EN_US"
    :vartype EN_US: str
    :cvar ES: "ES"
    :vartype ES: str
    :cvar ES_AR: "ES_AR"
    :vartype ES_AR: str
    :cvar ES_MX: "ES_MX"
    :vartype ES_MX: str
    :cvar ET: "ET"
    :vartype ET: str
    :cvar FI: "FI"
    :vartype FI: str
    :cvar FR: "FR"
    :vartype FR: str
    :cvar HE: "HE"
    :vartype HE: str
    :cvar HI: "HI"
    :vartype HI: str
    :cvar HR: "HR"
    :vartype HR: str
    :cvar HU: "HU"
    :vartype HU: str
    :cvar ID: "ID"
    :vartype ID: str
    :cvar IS: "IS"
    :vartype IS: str
    :cvar IT: "IT"
    :vartype IT: str
    :cvar JA: "JA"
    :vartype JA: str
    :cvar KA: "KA"
    :vartype KA: str
    :cvar KO: "KO"
    :vartype KO: str
    :cvar LT: "LT"
    :vartype LT: str
    :cvar LV: "LV"
    :vartype LV: str
    :cvar MS: "MS"
    :vartype MS: str
    :cvar NL: "NL"
    :vartype NL: str
    :cvar NO: "NO"
    :vartype NO: str
    :cvar PL: "PL"
    :vartype PL: str
    :cvar PT_BR: "PT_BR"
    :vartype PT_BR: str
    :cvar PT_PT: "PT_PT"
    :vartype PT_PT: str
    :cvar RO: "RO"
    :vartype RO: str
    :cvar RU: "RU"
    :vartype RU: str
    :cvar SK: "SK"
    :vartype SK: str
    :cvar SL: "SL"
    :vartype SL: str
    :cvar SR: "SR"
    :vartype SR: str
    :cvar SV: "SV"
    :vartype SV: str
    :cvar TH: "TH"
    :vartype TH: str
    :cvar TL: "TL"
    :vartype TL: str
    :cvar TR: "TR"
    :vartype TR: str
    :cvar UK: "UK"
    :vartype UK: str
    :cvar VI: "VI"
    :vartype VI: str
    :cvar ZH_CN: "ZH_CN"
    :vartype ZH_CN: str
    :cvar ZH_TW: "ZH_TW"
    :vartype ZH_TW: str
    """

    AR = "AR"
    BG = "BG"
    CA = "CA"
    CS = "CS"
    DA = "DA"
    DE = "DE"
    EL = "EL"
    EN = "EN"
    EN_GB = "EN_GB"
    EN_US = "EN_US"
    ES = "ES"
    ES_AR = "ES_AR"
    ES_MX = "ES_MX"
    ET = "ET"
    FI = "FI"
    FR = "FR"
    HE = "HE"
    HI = "HI"
    HR = "HR"
    HU = "HU"
    ID = "ID"
    IS = "IS"
    IT = "IT"
    JA = "JA"
    KA = "KA"
    KO = "KO"
    LT = "LT"
    LV = "LV"
    MS = "MS"
    NL = "NL"
    NO = "NO"
    PL = "PL"
    PT_BR = "PT_BR"
    PT_PT = "PT_PT"
    RO = "RO"
    RU = "RU"
    SK = "SK"
    SL = "SL"
    SR = "SR"
    SV = "SV"
    TH = "TH"
    TL = "TL"
    TR = "TR"
    UK = "UK"
    VI = "VI"
    ZH_CN = "ZH_CN"
    ZH_TW = "ZH_TW"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, HotelsInputDtoLanguage._member_map_.values())
        )


class HotelsInputDtoExtras(Enum):
    """An enumeration representing different categories.

    :cvar HOTEL_INFO: "HOTEL_INFO"
    :vartype HOTEL_INFO: str
    :cvar ROOM_INFO: "ROOM_INFO"
    :vartype ROOM_INFO: str
    :cvar KEY_COLLECTION_INFO: "KEY_COLLECTION_INFO"
    :vartype KEY_COLLECTION_INFO: str
    :cvar HOTEL_FACILITIES: "HOTEL_FACILITIES"
    :vartype HOTEL_FACILITIES: str
    :cvar HOTEL_PHOTOS: "HOTEL_PHOTOS"
    :vartype HOTEL_PHOTOS: str
    :cvar HOTEL_DESCRIPTION: "HOTEL_DESCRIPTION"
    :vartype HOTEL_DESCRIPTION: str
    """

    HOTEL_INFO = "HOTEL_INFO"
    ROOM_INFO = "ROOM_INFO"
    KEY_COLLECTION_INFO = "KEY_COLLECTION_INFO"
    HOTEL_FACILITIES = "HOTEL_FACILITIES"
    HOTEL_PHOTOS = "HOTEL_PHOTOS"
    HOTEL_DESCRIPTION = "HOTEL_DESCRIPTION"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, HotelsInputDtoExtras._member_map_.values()))


@JsonMap({})
class HotelsInputDto(BaseModel):
    """HotelsInputDto

    :param hotel_ids: A list of up to 1000 hotel ids., defaults to None
    :type hotel_ids: List[int], optional
    :param language: The language code to return the results in. Please check the "Possible Values" section of the documentation for the accepted language codes. , defaults to None
    :type language: HotelsInputDtoLanguage, optional
    :param extras: Returns extra bits of information about hotels., defaults to None
    :type extras: List[HotelsInputDtoExtras], optional
    :param offset: The number of rows to offset the results by. NOTE: this needs to be 0 or a multiple of 100., defaults to None
    :type offset: int, optional
    :param rows: The maximum number of rows to return. NOTE: this needs to be a multiple of 100., defaults to None
    :type rows: int, optional
    """

    def __init__(
        self,
        hotel_ids: List[int] = None,
        language: HotelsInputDtoLanguage = None,
        extras: List[HotelsInputDtoExtras] = None,
        offset: int = None,
        rows: int = None,
    ):
        if hotel_ids is not None:
            self.hotel_ids = hotel_ids
        if language is not None:
            self.language = self._enum_matching(
                language, HotelsInputDtoLanguage.list(), "language"
            )
        if extras is not None:
            self.extras = self._define_list(extras, HotelsInputDtoExtras)
        if offset is not None:
            self.offset = offset
        if rows is not None:
            self.rows = rows
