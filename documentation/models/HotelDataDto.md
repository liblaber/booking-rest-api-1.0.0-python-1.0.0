# HotelDataDto

Hotel specific information.

**Properties**

| Name                   | Type                    | Required | Description                                              |
| :--------------------- | :---------------------- | :------- | :------------------------------------------------------- |
| address                | str                     | ❌       | The street address of the hotel.                         |
| city_id                | int                     | ❌       | Id of the city where this property is located.           |
| country                | str                     | ❌       | Two-letter ISO country code of the hotel.                |
| location               | CoordinatesDto          | ❌       | A signed integer number that uniquely identifies a city. |
| zip                    | str                     | ❌       | Hotel ZIP code                                           |
| currency               | str                     | ❌       | Three-letter ISO currency code for the hotel.            |
| checkin_checkout_times | CheckinCheckoutTimesDto | ❌       |                                                          |
| hotel_photos           | List[HotelPhotoDto]     | ❌       | Photos specific information of the hotel.                |
| hotel_description      | str                     | ❌       | The description text for this hotel.                     |
| url                    | str                     | ❌       | URL of the hotel's page on Booking.com.                  |
| deep_link_url          | str                     | ❌       | Deep link mobile app URL.                                |
| region_ids             | List[int]               | ❌       | List of region_ids that the hotel belongs to             |
| number_of_reviews      | int                     | ❌       | Number of reviews for this hotel.                        |
| review_score           | float                   | ❌       | Review score of this hotel.                              |
| spoken_languages       | List[str]               | ❌       | Languages spoken by the hotel's staff                    |

<!-- This file was generated by liblab | https://liblab.com/ -->
