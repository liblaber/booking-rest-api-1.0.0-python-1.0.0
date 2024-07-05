# SearchInputDto

**Properties**

| Name                     | Type                       | Required | Description                                                                                                                                                                                                                                                                                                                                         |
| :----------------------- | :------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| checkin                  | str                        | ✅       | The checkin date. Must be within 500 days in the future and in the format yyyy-mm-dd.                                                                                                                                                                                                                                                               |
| checkout                 | str                        | ✅       | The checkout date. Must be later than {checkin}. Must be between 1 and 90 days after {checkin}. Must be within 500 days in the future and in the format yyyy-mm-dd.                                                                                                                                                                                 |
| booker                   | BookerInputDto             | ✅       | The booker's information.                                                                                                                                                                                                                                                                                                                           |
| guests                   | GuestsInputDto             | ✅       | The guest details for the request.                                                                                                                                                                                                                                                                                                                  |
| currency                 | str                        | ❌       | A three-letter code that uniquely identifies a monetary currency as defined by the ISO 4217 standard.                                                                                                                                                                                                                                               |
| city                     | int                        | ❌       | A signed integer number that uniquely identifies a city.                                                                                                                                                                                                                                                                                            |
| country                  | str                        | ❌       | A two-letter code that uniquely identifies a country. This code is defined by the ISO 3166-1 alpha-2 standard (ISO2) as described here: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2.                                                                                                                                                           |
| extras                   | List[SearchInputDtoExtras] | ❌       | Input parameter to request for additional information about the products.                                                                                                                                                                                                                                                                           |
| accommodations           | List[int]                  | ❌       | A signed integer number that uniquely identifies an accommodation property.                                                                                                                                                                                                                                                                         |
| accommodation_facilities | List[int]                  | ❌       | A signed integer number that uniquely identifies an accommodation facility.                                                                                                                                                                                                                                                                         |
| room_facilities          | List[int]                  | ❌       | A signed integer number that uniquely identifies a room facility.                                                                                                                                                                                                                                                                                   |
| accommodation_types      | List[int]                  | ❌       | A signed integer number that uniquely identifies an accommodation type.                                                                                                                                                                                                                                                                             |
| brands                   | List[int]                  | ❌       | A signed integer number that uniquely identifies a brand.                                                                                                                                                                                                                                                                                           |
| airport                  | str                        | ❌       | A three-letter code that uniquely identifies an airport as defined by the International Air Transport Association (IATA).                                                                                                                                                                                                                           |
| district                 | int                        | ❌       | A signed integer number that uniquely identifies a district. Typically, districts define known areas within a city.                                                                                                                                                                                                                                 |
| landmark                 | int                        | ❌       | A signed integer number that uniquely identifies a relevant geographical landmark, like a monument or a natural attraction.                                                                                                                                                                                                                         |
| coordinates              | Coordinates                | ❌       | Limit the result list to the specified coordinates.                                                                                                                                                                                                                                                                                                 |
| region                   | int                        | ❌       | A signed integer number that uniquely identifies a geographical region. Regions usually define official administrative areas within a country, but may also include multiple countries and in some cases un-official but popular designations for geographical areas. An example of a region that crosses multiple countries is the Alps in Europe. |
| rows                     | int                        | ❌       | The maximum number of results to return.                                                                                                                                                                                                                                                                                                            |
| page                     | str                        | ❌       | Pagination token used to retrieve the next page of results. Obtained from `next_page`.                                                                                                                                                                                                                                                              |

# SearchInputDtoExtras

Input parameter to request for additional information about the products.

**Properties**

| Name          | Type | Required | Description     |
| :------------ | :--- | :------- | :-------------- |
| EXTRA_CHARGES | str  | ✅       | "EXTRA_CHARGES" |
| PRODUCTS      | str  | ✅       | "PRODUCTS"      |

<!-- This file was generated by liblab | https://liblab.com/ -->