# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class Meals(Enum):
    """An enumeration representing different categories.

    :cvar BREAKFAST: "BREAKFAST"
    :vartype BREAKFAST: str
    :cvar DINNER: "DINNER"
    :vartype DINNER: str
    :cvar LUNCH: "LUNCH"
    :vartype LUNCH: str
    """

    BREAKFAST = "BREAKFAST"
    DINNER = "DINNER"
    LUNCH = "LUNCH"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Meals._member_map_.values()))


class Plan(Enum):
    """An enumeration representing different categories.

    :cvar ALL_INCLUSIVE: "ALL_INCLUSIVE"
    :vartype ALL_INCLUSIVE: str
    :cvar BREAKFAST_INCLUDED: "BREAKFAST_INCLUDED"
    :vartype BREAKFAST_INCLUDED: str
    :cvar FULL_BOARD: "FULL_BOARD"
    :vartype FULL_BOARD: str
    :cvar HALF_BOARD: "HALF_BOARD"
    :vartype HALF_BOARD: str
    :cvar NO_PLAN: "NO_PLAN"
    :vartype NO_PLAN: str
    """

    ALL_INCLUSIVE = "ALL_INCLUSIVE"
    BREAKFAST_INCLUDED = "BREAKFAST_INCLUDED"
    FULL_BOARD = "FULL_BOARD"
    HALF_BOARD = "HALF_BOARD"
    NO_PLAN = "NO_PLAN"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Plan._member_map_.values()))


@JsonMap({})
class MealPlanDto(BaseModel):
    """The meal plan policy for this product.

    :param meals: The meals included in the meal plan., defaults to None
    :type meals: List[Meals], optional
    :param plan: The meal plan included in this product., defaults to None
    :type plan: Plan, optional
    """

    def __init__(self, meals: List[Meals] = None, plan: Plan = None):
        if meals is not None:
            self.meals = self._define_list(meals, Meals)
        if plan is not None:
            self.plan = self._enum_matching(plan, Plan.list(), "plan")
