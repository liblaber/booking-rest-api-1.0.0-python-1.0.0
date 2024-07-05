# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .meta import Meta
from .review_scores_output_dto import ReviewScoresOutputDto


@JsonMap({})
class ResponseOutputV2ReviewScoresOutputDto(BaseModel):
    """ResponseOutputV2ReviewScoresOutputDto

    :param meta: meta, defaults to None
    :type meta: Meta, optional
    :param result: result, defaults to None
    :type result: List[ReviewScoresOutputDto], optional
    """

    def __init__(self, meta: Meta = None, result: List[ReviewScoresOutputDto] = None):
        if meta is not None:
            self.meta = self._define_object(meta, Meta)
        if result is not None:
            self.result = self._define_list(result, ReviewScoresOutputDto)