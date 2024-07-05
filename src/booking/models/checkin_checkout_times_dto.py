# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .local_time import LocalTime


@JsonMap({})
class CheckinCheckoutTimesDto(BaseModel):
    """CheckinCheckoutTimesDto

    :param checkin_from: The time till when checkout can be done at this property., defaults to None
    :type checkin_from: LocalTime, optional
    :param checkin_to: The time till when checkout can be done at this property., defaults to None
    :type checkin_to: LocalTime, optional
    :param checkout_from: The time till when checkout can be done at this property., defaults to None
    :type checkout_from: LocalTime, optional
    :param checkout_to: The time till when checkout can be done at this property., defaults to None
    :type checkout_to: LocalTime, optional
    """

    def __init__(
        self,
        checkin_from: LocalTime = None,
        checkin_to: LocalTime = None,
        checkout_from: LocalTime = None,
        checkout_to: LocalTime = None,
    ):
        if checkin_from is not None:
            self.checkin_from = self._define_object(checkin_from, LocalTime)
        if checkin_to is not None:
            self.checkin_to = self._define_object(checkin_to, LocalTime)
        if checkout_from is not None:
            self.checkout_from = self._define_object(checkout_from, LocalTime)
        if checkout_to is not None:
            self.checkout_to = self._define_object(checkout_to, LocalTime)