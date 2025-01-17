# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .question_dto import QuestionDto


@JsonMap({})
class ScoreBreakdown(BaseModel):
    """A breakdown of scores per reviewer type and review question.

    :param average_score: Average score from this reviewer type., defaults to None
    :type average_score: float, optional
    :param count: Number of responses from this reviewer type., defaults to None
    :type count: int, optional
    :param question: Review scores per question., defaults to None
    :type question: List[QuestionDto], optional
    :param reviewer_type: Reviewer type., defaults to None
    :type reviewer_type: str, optional
    """

    def __init__(
        self,
        average_score: float = None,
        count: int = None,
        question: List[QuestionDto] = None,
        reviewer_type: str = None,
    ):
        if average_score is not None:
            self.average_score = average_score
        if count is not None:
            self.count = count
        if question is not None:
            self.question = self._define_list(question, QuestionDto)
        if reviewer_type is not None:
            self.reviewer_type = reviewer_type
