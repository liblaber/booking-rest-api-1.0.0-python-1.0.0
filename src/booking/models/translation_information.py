# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .translated_string import TranslatedString


@JsonMap({})
class TranslationInformation(BaseModel):
    """Text containing important information about the property. The value is translated in the requested languages.

    :param translated_string: Translated description of this room. The maximum number of characters returned may be limited by contract., defaults to None
    :type translated_string: TranslatedString, optional
    :param non_lazy_translations: non_lazy_translations, defaults to None
    :type non_lazy_translations: dict, optional
    """

    def __init__(
        self,
        translated_string: TranslatedString = None,
        non_lazy_translations: dict = None,
    ):
        if translated_string is not None:
            self.translated_string = self._define_object(
                translated_string, TranslatedString
            )
        if non_lazy_translations is not None:
            self.non_lazy_translations = non_lazy_translations
