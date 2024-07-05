# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .cancellation_dto import CancellationDto
from .meal_plan_dto import MealPlanDto
from .payment_dto import PaymentDto


@JsonMap({})
class PoliciesDto(BaseModel):
    """The policies for this product.

    :param cancellation: The cancellation policy for this product., defaults to None
    :type cancellation: CancellationDto, optional
    :param meal_plan: The meal plan policy for this product., defaults to None
    :type meal_plan: MealPlanDto, optional
    :param payment: Payment terms and conditions for this product., defaults to None
    :type payment: PaymentDto, optional
    """

    def __init__(
        self,
        cancellation: CancellationDto = None,
        meal_plan: MealPlanDto = None,
        payment: PaymentDto = None,
    ):
        if cancellation is not None:
            self.cancellation = self._define_object(cancellation, CancellationDto)
        if meal_plan is not None:
            self.meal_plan = self._define_object(meal_plan, MealPlanDto)
        if payment is not None:
            self.payment = self._define_object(payment, PaymentDto)