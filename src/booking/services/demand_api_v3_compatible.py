# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.search_input_dto import SearchInputDto
from ..models.search_accept import SearchAccept
from ..models.response_output_list_search_output_dto import (
    ResponseOutputListSearchOutputDto,
)
from ..models.response_output_list_details_output_dto import (
    ResponseOutputListDetailsOutputDto,
)
from ..models.response_output_constants_output_dto import (
    ResponseOutputConstantsOutputDto,
)
from ..models.post_details_accept import PostDetailsAccept
from ..models.get_accommodation_constants_accept import GetAccommodationConstantsAccept
from ..models.details_input_dto import DetailsInputDto
from ..models.constant_input_dto import ConstantInputDto


class DemandApiV3CompatibleService(BaseService):

    @cast_models
    def search(
        self, request_body: SearchInputDto, accept: SearchAccept = None
    ) -> ResponseOutputListSearchOutputDto:
        """This endpoint returns the cheapest available product for each hotel matching the search criteria.

        :param request_body: The request body.
        :type request_body: SearchInputDto
        :param accept: accept, defaults to None
        :type accept: SearchAccept, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: ResponseOutputListSearchOutputDto
        """

        Validator(SearchInputDto).validate(request_body)
        Validator(SearchAccept).is_optional().validate(accept)

        serialized_request = (
            Serializer(
                f"{self.base_url}/demand-api-v3-compatible/search",
                self.get_default_headers(),
            )
            .add_header("Accept", accept)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return ResponseOutputListSearchOutputDto._unmap(response)

    @cast_models
    def post_details(
        self, request_body: DetailsInputDto, accept: PostDetailsAccept = None
    ) -> ResponseOutputListDetailsOutputDto:
        """This endpoint returns detailed information on all accommodation properties matching a given search criteria.
        By default, only basic information is returned. To receive extended information use the `extras` parameter.
        Is is mandatory to pass one of the input parameters: accommodations, airport, city, country or region.

        :param request_body: The request body.
        :type request_body: DetailsInputDto
        :param accept: accept, defaults to None
        :type accept: PostDetailsAccept, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: ResponseOutputListDetailsOutputDto
        """

        Validator(DetailsInputDto).validate(request_body)
        Validator(PostDetailsAccept).is_optional().validate(accept)

        serialized_request = (
            Serializer(
                f"{self.base_url}/demand-api-v3-compatible/details",
                self.get_default_headers(),
            )
            .add_header("Accept", accept)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return ResponseOutputListDetailsOutputDto._unmap(response)

    @cast_models
    def get_accommodation_constants(
        self,
        request_body: ConstantInputDto = None,
        accept: GetAccommodationConstantsAccept = None,
    ) -> ResponseOutputConstantsOutputDto:
        """This endpoint enumerates the internal codes and names, in the selected languages,
        for relevant accommodation specific types.

        These accommodation specific types include the list of facilities
        that may be available at a property like "Elevator" or "Swimmingpool Outdoor".

        For example, the following parameters will return
        the full list in English (US) and French: `{"languages":"en-us","fr"}`.

        To get the full list call the endpoint passing an empty body.
        The codes returned are what is used as input and output for other endpoints in the accommodations namespace.

        :param request_body: The request body., defaults to None
        :type request_body: ConstantInputDto, optional
        :param accept: accept, defaults to None
        :type accept: GetAccommodationConstantsAccept, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: ResponseOutputConstantsOutputDto
        """

        Validator(ConstantInputDto).is_optional().validate(request_body)
        Validator(GetAccommodationConstantsAccept).is_optional().validate(accept)

        serialized_request = (
            Serializer(
                f"{self.base_url}/demand-api-v3-compatible/constants",
                self.get_default_headers(),
            )
            .add_header("Accept", accept)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return ResponseOutputConstantsOutputDto._unmap(response)
