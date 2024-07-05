# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class ReviewScoresInputDtoLanguage(Enum):
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
            map(lambda x: x.value, ReviewScoresInputDtoLanguage._member_map_.values())
        )


class ReviewerType(Enum):
    """An enumeration representing different categories.

    :cvar SOLO_TRAVELLER: "SOLO_TRAVELLER"
    :vartype SOLO_TRAVELLER: str
    :cvar YOUNG_COUPLE: "YOUNG_COUPLE"
    :vartype YOUNG_COUPLE: str
    :cvar MATURE_COUPLE: "MATURE_COUPLE"
    :vartype MATURE_COUPLE: str
    :cvar FAMILY_WITH_YOUNG_CHILDREN: "FAMILY_WITH_YOUNG_CHILDREN"
    :vartype FAMILY_WITH_YOUNG_CHILDREN: str
    :cvar FAMILY_WITH_OLDER_CHILDREN: "FAMILY_WITH_OLDER_CHILDREN"
    :vartype FAMILY_WITH_OLDER_CHILDREN: str
    :cvar WITH_FRIENDS: "WITH_FRIENDS"
    :vartype WITH_FRIENDS: str
    :cvar GROUP: "GROUP"
    :vartype GROUP: str
    :cvar REVIEW_CATEGORY_COUPLES: "REVIEW_CATEGORY_COUPLES"
    :vartype REVIEW_CATEGORY_COUPLES: str
    :cvar REVIEW_CATEGORY_FAMILIES: "REVIEW_CATEGORY_FAMILIES"
    :vartype REVIEW_CATEGORY_FAMILIES: str
    :cvar REVIEW_CATEGORY_GROUP_OF_FRIENDS: "REVIEW_CATEGORY_GROUP_OF_FRIENDS"
    :vartype REVIEW_CATEGORY_GROUP_OF_FRIENDS: str
    :cvar REVIEW_CATEGORY_BUSINESS_TRAVELLERS: "REVIEW_CATEGORY_BUSINESS_TRAVELLERS"
    :vartype REVIEW_CATEGORY_BUSINESS_TRAVELLERS: str
    """

    SOLO_TRAVELLER = "SOLO_TRAVELLER"
    YOUNG_COUPLE = "YOUNG_COUPLE"
    MATURE_COUPLE = "MATURE_COUPLE"
    FAMILY_WITH_YOUNG_CHILDREN = "FAMILY_WITH_YOUNG_CHILDREN"
    FAMILY_WITH_OLDER_CHILDREN = "FAMILY_WITH_OLDER_CHILDREN"
    WITH_FRIENDS = "WITH_FRIENDS"
    GROUP = "GROUP"
    REVIEW_CATEGORY_COUPLES = "REVIEW_CATEGORY_COUPLES"
    REVIEW_CATEGORY_FAMILIES = "REVIEW_CATEGORY_FAMILIES"
    REVIEW_CATEGORY_GROUP_OF_FRIENDS = "REVIEW_CATEGORY_GROUP_OF_FRIENDS"
    REVIEW_CATEGORY_BUSINESS_TRAVELLERS = "REVIEW_CATEGORY_BUSINESS_TRAVELLERS"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ReviewerType._member_map_.values()))


@JsonMap({})
class ReviewScoresInputDto(BaseModel):
    """ReviewScoresInputDto

    :param hotel_ids: List of hotel ids for which review score information should be displayed.
    :type hotel_ids: List[int]
    :param affiliate_id: Can be used to specify the affiliate id that should be used instead of the default one., defaults to None
    :type affiliate_id: int, optional
    :param language: Code of the language used to render response. Please check the "Possible Values" section of the documentation for the accepted language codes. , defaults to None
    :type language: ReviewScoresInputDtoLanguage, optional
    :param reviewer_type: Limits reviews to those written by specific reviewer type., defaults to None
    :type reviewer_type: ReviewerType, optional
    """

    def __init__(
        self,
        hotel_ids: List[int],
        affiliate_id: int = None,
        language: ReviewScoresInputDtoLanguage = None,
        reviewer_type: ReviewerType = None,
    ):
        self.hotel_ids = hotel_ids
        if affiliate_id is not None:
            self.affiliate_id = affiliate_id
        if language is not None:
            self.language = self._enum_matching(
                language, ReviewScoresInputDtoLanguage.list(), "language"
            )
        if reviewer_type is not None:
            self.reviewer_type = self._enum_matching(
                reviewer_type, ReviewerType.list(), "reviewer_type"
            )