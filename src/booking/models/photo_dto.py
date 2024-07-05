# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .photo_url_dto import PhotoUrlDto


@JsonMap({})
class PhotoDto(BaseModel):
    """PhotoDto

    :param main_photo: Flags this as the main photo. Not returned otherwise., defaults to None
    :type main_photo: bool, optional
    :param tags: A list of tags associated with the photo. Manually generated., defaults to None
    :type tags: List[str], optional
    :param url: url, defaults to None
    :type url: PhotoUrlDto, optional
    """

    def __init__(
        self, main_photo: bool = None, tags: List[str] = None, url: PhotoUrlDto = None
    ):
        if main_photo is not None:
            self.main_photo = main_photo
        if tags is not None:
            self.tags = tags
        if url is not None:
            self.url = self._define_object(url, PhotoUrlDto)