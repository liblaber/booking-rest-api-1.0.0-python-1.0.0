# DemandApiV3CompatibleService

A list of all methods in the `DemandApiV3CompatibleService` service. Click on the method name to view detailed information about that method.

| Methods                       | Description                                                                                                  |
| :---------------------------- | :----------------------------------------------------------------------------------------------------------- |
| [search](#search)             | This endpoint returns the cheapest available product for each hotel matching the search criteria.            |
| [post_details](#post_details) | This endpoint returns detailed information on all accommodation properties matching a given search criteria. |

By default, only basic information is returned. To receive extended information use the `extras` parameter.
Is is mandatory to pass one of the input parameters: accommodations, airport, city, country or region.
|
|[get_accommodation_constants](#get_accommodation_constants)| This endpoint enumerates the internal codes and names, in the selected languages,
for relevant accommodation specific types.

These accommodation specific types include the list of facilities
that may be available at a property like "Elevator" or "Swimmingpool Outdoor".

For example, the following parameters will return
the full list in English (US) and French: `{"languages":"en-us","fr"}`.

To get the full list call the endpoint passing an empty body.
The codes returned are what is used as input and output for other endpoints in the accommodations namespace.
|

## search

This endpoint returns the cheapest available product for each hotel matching the search criteria.

- HTTP Method: `POST`
- Endpoint: `/demand-api-v3-compatible/search`

**Parameters**

| Name         | Type                                          | Required | Description       |
| :----------- | :-------------------------------------------- | :------- | :---------------- |
| request_body | [SearchInputDto](../models/SearchInputDto.md) | ✅       | The request body. |
| accept       | [SearchAccept](../models/SearchAccept.md)     | ❌       |                   |

**Return Type**

`ResponseOutputListSearchOutputDto`

**Example Usage Code Snippet**

```python
from booking import Booking, Environment
from booking.models import SearchInputDto, SearchAccept

sdk = Booking(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = SearchInputDto(
    checkin="checkin",
    checkout="checkout",
    booker={
        "country": "xb",
        "platform": "ANDROID",
        "travel_purpose": "BUSINESS",
        "user_groups": [
            "AUTHENTICATED"
        ]
    },
    currency="EUR",
    city=1,
    country="nl",
    guests={
        "number_of_adults": 10,
        "number_of_rooms": 10,
        "allocation": [
            {
                "children": [
                    8
                ],
                "number_of_adults": 4
            }
        ],
        "children": [
            14
        ]
    },
    extras=[
        "EXTRA_CHARGES"
    ],
    accommodations=[
        7
    ],
    accommodation_facilities=[
        0
    ],
    room_facilities=[
        1
    ],
    accommodation_types=[
        2
    ],
    brands=[
        5
    ],
    airport="AMS",
    district=2,
    landmark=10,
    coordinates={
        "latitude": 5.31,
        "longitude": 2.65,
        "radius": 8.29
    },
    region=0,
    rows=845,
    page="page"
)

result = sdk.demand_api_v3_compatible.search(
    request_body=request_body,
    accept="application/json"
)

print(result)
```

## post_details

This endpoint returns detailed information on all accommodation properties matching a given search criteria.
By default, only basic information is returned. To receive extended information use the `extras` parameter.
Is is mandatory to pass one of the input parameters: accommodations, airport, city, country or region.

- HTTP Method: `POST`
- Endpoint: `/demand-api-v3-compatible/details`

**Parameters**

| Name         | Type                                                | Required | Description       |
| :----------- | :-------------------------------------------------- | :------- | :---------------- |
| request_body | [DetailsInputDto](../models/DetailsInputDto.md)     | ✅       | The request body. |
| accept       | [PostDetailsAccept](../models/PostDetailsAccept.md) | ❌       |                   |

**Return Type**

`ResponseOutputListDetailsOutputDto`

**Example Usage Code Snippet**

```python
from booking import Booking, Environment
from booking.models import DetailsInputDto, PostDetailsAccept

sdk = Booking(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = DetailsInputDto(
    accommodations=[
        6
    ],
    accommodation_facilities=[
        7
    ],
    accommodation_types=[
        10
    ],
    airport="AMS",
    brands=[
        5
    ],
    city=0,
    country="nl",
    region=7,
    extras=[
        "DESCRIPTION"
    ],
    languages=[
        "AR"
    ],
    rows=963,
    page="page"
)

result = sdk.demand_api_v3_compatible.post_details(
    request_body=request_body,
    accept="application/json"
)

print(result)
```

## get_accommodation_constants

This endpoint enumerates the internal codes and names, in the selected languages,
for relevant accommodation specific types.

These accommodation specific types include the list of facilities
that may be available at a property like "Elevator" or "Swimmingpool Outdoor".

For example, the following parameters will return
the full list in English (US) and French: `{"languages":"en-us","fr"}`.

To get the full list call the endpoint passing an empty body.
The codes returned are what is used as input and output for other endpoints in the accommodations namespace.

- HTTP Method: `POST`
- Endpoint: `/demand-api-v3-compatible/constants`

**Parameters**

| Name         | Type                                                                            | Required | Description       |
| :----------- | :------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [ConstantInputDto](../models/ConstantInputDto.md)                               | ❌       | The request body. |
| accept       | [GetAccommodationConstantsAccept](../models/GetAccommodationConstantsAccept.md) | ❌       |                   |

**Return Type**

`ResponseOutputConstantsOutputDto`

**Example Usage Code Snippet**

```python
from booking import Booking, Environment
from booking.models import ConstantInputDto, GetAccommodationConstantsAccept

sdk = Booking(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = ConstantInputDto(
    constants=[
        "ACCOMMODATION_TYPES"
    ],
    languages=[
        "AR"
    ]
)

result = sdk.demand_api_v3_compatible.get_accommodation_constants(
    request_body=request_body,
    accept="application/json"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
