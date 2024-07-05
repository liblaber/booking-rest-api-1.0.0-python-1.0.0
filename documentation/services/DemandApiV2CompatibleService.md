# DemandApiV2CompatibleService

A list of all methods in the `DemandApiV2CompatibleService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                                               |
| :---------------------------------------------------- | :------------------------------------------------------------------------ |
| [get_hotels_review_scores](#get_hotels_review_scores) | Gives information about review scores for specified hotel_ids and filter. |

The information consists of score breakdown per reviewer_type and review questions,
and overall score distribution per score value (1 - 10).

The available filter is input parameter reviewer_type=... .
It allows generating review score information for just one reviewer type.

Language in which the response is rendered can be controlled with the input parameter language=...
(default: 'en'). Setting the language will reflect on the output fields question and review_score_word.

One additional output field can be requested with input parameter extras=review_score_word.
|
|[get_hotels](#get_hotels)| This call returns the hotel and room data. By default, only hotel_id is returned in the output.

One of the argument: hotel_ids, city_ids, country_ids, region_ids, district_ids, chain_ids is mandatory.

Additional data needs to be requested via extras parameter.

The data is returned in English by default.
|
|[get_hotel_types](#get_hotel_types)| This endpoint returns hotel types names and their translations. (EN is default) |
|[get_hotel_theme_types](#get_hotel_theme_types)| This endpoint returns a list of hotel theme types (in English). |
|[get_room_facility_types](#get_room_facility_types)| This endpoint returns room facility types names and their translations (EN is default). |
|[get_hotel_availability](#get_hotel_availability)| This endpoint returns the cheapest available room for each hotel matching your check-in and check-out dates.
You can search for hotels in a city, or for a specific list of (upto 300) hotels by hotel_ids.
Here you will find whether the price included breakfast or other meals, as well as whether it is possible to cancel for free.
It is possible to have a breakdown of the price returned by this endpoint and to filter by property types and/or hotel facilities.
|
|[get_block_availability](#get_block_availability)| This endpoint is where you find a list of all bookable or available rooms at a property.
A room can have multiple blocks, as a block is a combination of the meal, cancellation policy, occupancy and other things.
You can find detailed information about one hotel per search (detail_level)
which will return most of the information needed to replicate the booking.com property page.

If you want to search multiple hotels, you can, but you get less detail.
For searching multiple hotels, it is recommended to use hotelAvailability.
|

## get_hotels_review_scores

Gives information about review scores for specified hotel_ids and filter.
The information consists of score breakdown per reviewer_type and review questions,
and overall score distribution per score value (1 - 10).

The available filter is input parameter reviewer_type=... .
It allows generating review score information for just one reviewer type.

Language in which the response is rendered can be controlled with the input parameter language=...
(default: 'en'). Setting the language will reflect on the output fields question and review_score_word.

One additional output field can be requested with input parameter extras=review_score_word.

- HTTP Method: `GET`
- Endpoint: `/demand-api-v2-compatible/reviewScores`

**Parameters**

| Name                    | Type                                                                    | Required | Description |
| :---------------------- | :---------------------------------------------------------------------- | :------- | :---------- |
| review_scores_input_dto | [ReviewScoresInputDto](../models/ReviewScoresInputDto.md)               | ✅       |             |
| accept                  | [GetHotelsReviewScoresAccept](../models/GetHotelsReviewScoresAccept.md) | ❌       |             |

**Return Type**

`ResponseOutputV2ReviewScoresOutputDto`

**Example Usage Code Snippet**

```python
from booking import Booking, Environment
from booking.models import ReviewScoresInputDto, GetHotelsReviewScoresAccept

sdk = Booking(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)
review_scores_input_dto=ReviewScoresInputDto(
    hotel_ids=[
        7
    ],
    affiliate_id=2,
    language="AR",
    reviewer_type="SOLO_TRAVELLER"
)

result = sdk.demand_api_v2_compatible.get_hotels_review_scores(
    review_scores_input_dto=review_scores_input_dto,
    accept="application/json, application/xml"
)

print(result)
```

## get_hotels

This call returns the hotel and room data. By default, only hotel_id is returned in the output.

One of the argument: hotel_ids, city_ids, country_ids, region_ids, district_ids, chain_ids is mandatory.

Additional data needs to be requested via extras parameter.

The data is returned in English by default.

- HTTP Method: `GET`
- Endpoint: `/demand-api-v2-compatible/hotels`

**Parameters**

| Name         | Type                                            | Required | Description |
| :----------- | :---------------------------------------------- | :------- | :---------- |
| hotels_input | [HotelsInputDto](../models/HotelsInputDto.md)   | ✅       |             |
| accept       | [GetHotelsAccept](../models/GetHotelsAccept.md) | ❌       |             |

**Return Type**

`ResponseOutputV2HotelsOutputDto`

**Example Usage Code Snippet**

```python
from booking import Booking, Environment
from booking.models import HotelsInputDto, GetHotelsAccept

sdk = Booking(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)
hotels_input=HotelsInputDto(
    hotel_ids=[
        7
    ],
    language="AR",
    extras=[
        "HOTEL_INFO"
    ],
    offset=6,
    rows=3
)

result = sdk.demand_api_v2_compatible.get_hotels(
    hotels_input=hotels_input,
    accept="application/json, application/xml"
)

print(result)
```

## get_hotel_types

This endpoint returns hotel types names and their translations. (EN is default)

- HTTP Method: `GET`
- Endpoint: `/demand-api-v2-compatible/hotelTypes`

**Parameters**

| Name                 | Type                                                    | Required | Description |
| :------------------- | :------------------------------------------------------ | :------- | :---------- |
| hotel_type_input_dto | [HotelTypeInputDto](../models/HotelTypeInputDto.md)     | ✅       |             |
| accept               | [GetHotelTypesAccept](../models/GetHotelTypesAccept.md) | ❌       |             |

**Return Type**

`ResponseOutputV2HotelTypesOutputDto`

**Example Usage Code Snippet**

```python
from booking import Booking, Environment
from booking.models import HotelTypeInputDto, GetHotelTypesAccept

sdk = Booking(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)
hotel_type_input_dto=HotelTypeInputDto(
    hotel_type_ids=[
        1
    ],
    languages=[
        "AR"
    ],
    offset=10,
    row=9
)

result = sdk.demand_api_v2_compatible.get_hotel_types(
    hotel_type_input_dto=hotel_type_input_dto,
    accept="application/json"
)

print(result)
```

## get_hotel_theme_types

This endpoint returns a list of hotel theme types (in English).

- HTTP Method: `GET`
- Endpoint: `/demand-api-v2-compatible/hotelThemeTypes`

**Parameters**

| Name                       | Type                                                              | Required | Description |
| :------------------------- | :---------------------------------------------------------------- | :------- | :---------- |
| hotel_theme_type_input_dto | [HotelThemeTypeInputDto](../models/HotelThemeTypeInputDto.md)     | ✅       |             |
| accept                     | [GetHotelThemeTypesAccept](../models/GetHotelThemeTypesAccept.md) | ❌       |             |

**Return Type**

`ResponseOutputV2HotelThemeTypesOutputDto`

**Example Usage Code Snippet**

```python
from booking import Booking, Environment
from booking.models import HotelThemeTypeInputDto, GetHotelThemeTypesAccept

sdk = Booking(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)
hotel_theme_type_input_dto=HotelThemeTypeInputDto(
    theme_ids=[
        9
    ],
    offset=4,
    row=1
)

result = sdk.demand_api_v2_compatible.get_hotel_theme_types(
    hotel_theme_type_input_dto=hotel_theme_type_input_dto,
    accept="application/json"
)

print(result)
```

## get_room_facility_types

This endpoint returns room facility types names and their translations (EN is default).

- HTTP Method: `GET`
- Endpoint: `/demand-api-v2-compatible/hotelFacilityTypes`

**Parameters**

| Name                     | Type                                                                  | Required | Description |
| :----------------------- | :-------------------------------------------------------------------- | :------- | :---------- |
| hotel_facility_input_dto | [HotelFacilityInputDto](../models/HotelFacilityInputDto.md)           | ✅       |             |
| accept                   | [GetRoomFacilityTypesAccept](../models/GetRoomFacilityTypesAccept.md) | ❌       |             |

**Return Type**

`ResponseOutputV2HotelFacilityTypeOutputDto`

**Example Usage Code Snippet**

```python
from booking import Booking, Environment
from booking.models import HotelFacilityInputDto, GetRoomFacilityTypesAccept

sdk = Booking(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)
hotel_facility_input_dto=HotelFacilityInputDto(
    facility_type_ids=[
        7
    ],
    hotel_facility_type_ids=[
        8
    ],
    languages=[
        "AR"
    ]
)

result = sdk.demand_api_v2_compatible.get_room_facility_types(
    hotel_facility_input_dto=hotel_facility_input_dto,
    accept="application/json"
)

print(result)
```

## get_hotel_availability

This endpoint returns the cheapest available room for each hotel matching your check-in and check-out dates.
You can search for hotels in a city, or for a specific list of (upto 300) hotels by hotel_ids.
Here you will find whether the price included breakfast or other meals, as well as whether it is possible to cancel for free.
It is possible to have a breakdown of the price returned by this endpoint and to filter by property types and/or hotel facilities.

- HTTP Method: `GET`
- Endpoint: `/demand-api-v2-compatible/hotelAvailability`

**Parameters**

| Name                         | Type                                                                  | Required | Description |
| :--------------------------- | :-------------------------------------------------------------------- | :------- | :---------- |
| hotel_availability_input_dto | [HotelAvailabilityInputDto](../models/HotelAvailabilityInputDto.md)   | ✅       |             |
| accept                       | [GetHotelAvailabilityAccept](../models/GetHotelAvailabilityAccept.md) | ❌       |             |

**Return Type**

`ResponseOutputV2HotelAvailabilityOutputDto`

**Example Usage Code Snippet**

```python
from booking import Booking, Environment
from booking.models import HotelAvailabilityInputDto, GetHotelAvailabilityAccept

sdk = Booking(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)
hotel_availability_input_dto=HotelAvailabilityInputDto(
    checkin="checkin",
    checkout="checkout",
    hotel_ids=[
        9
    ],
    currency="currency",
    guest_country="guest_country",
    no_rooms=4,
    user_platform="ANDROID",
    rows=409,
    page="page"
)

result = sdk.demand_api_v2_compatible.get_hotel_availability(
    hotel_availability_input_dto=hotel_availability_input_dto,
    accept="application/json"
)

print(result)
```

## get_block_availability

This endpoint is where you find a list of all bookable or available rooms at a property.
A room can have multiple blocks, as a block is a combination of the meal, cancellation policy, occupancy and other things.
You can find detailed information about one hotel per search (detail_level)
which will return most of the information needed to replicate the booking.com property page.

If you want to search multiple hotels, you can, but you get less detail.
For searching multiple hotels, it is recommended to use hotelAvailability.

- HTTP Method: `GET`
- Endpoint: `/demand-api-v2-compatible/blockAvailability`

**Parameters**

| Name        | Type                                                                  | Required | Description |
| :---------- | :-------------------------------------------------------------------- | :------- | :---------- |
| block_input | [BlockAvailabilityInputDto](../models/BlockAvailabilityInputDto.md)   | ✅       |             |
| accept      | [GetBlockAvailabilityAccept](../models/GetBlockAvailabilityAccept.md) | ❌       |             |

**Return Type**

`ResponseOutputV2BlockAvailabilityOutputDto`

**Example Usage Code Snippet**

```python
from booking import Booking, Environment
from booking.models import BlockAvailabilityInputDto, GetBlockAvailabilityAccept

sdk = Booking(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)
block_input=BlockAvailabilityInputDto(
    hotel_ids=[
        0
    ],
    checkin="checkin",
    checkout="checkout",
    guest_cc="guest_cc",
    currency="currency",
    extras=[
        "ADDON_TYPE"
    ],
    affiliate_id="affiliate_id",
    block_ids=[
        "5555555_55555555_5_5_5,6666666_66666666_6_6_6"
    ],
    guest_ip="guest_ip",
    guest_qty=[
        4
    ],
    language="AR",
    num_rooms=10,
    room1=[
        "room1"
    ],
    user_platform="ANDROID"
)

result = sdk.demand_api_v2_compatible.get_block_availability(
    block_input=block_input,
    accept="application/json, application/xml"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
