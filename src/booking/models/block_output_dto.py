# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class BlockOutputDto(BaseModel):
    """The object containing all the relevant information for the combination of room, policy, meal and occupancy that determines the price."
    A block is the unique entity you book with booking.com.

    :param block_id: block_id, defaults to None
    :type block_id: str, optional
    :param breakfast_included: breakfast_included, defaults to None
    :type breakfast_included: bool, optional
    """

    def __init__(self, block_id: str = None, breakfast_included: bool = None):
        if block_id is not None:
            self.block_id = block_id
        if breakfast_included is not None:
            self.breakfast_included = breakfast_included
