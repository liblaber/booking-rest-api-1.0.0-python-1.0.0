# DetailsInputDto

**Properties**

| Name                     | Type                           | Required | Description                                                                                                                                                                                                                                                                                                                                         |
| :----------------------- | :----------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| accommodations           | List[int]                      | ❌       | A signed integer number that uniquely identifies an accommodation property.                                                                                                                                                                                                                                                                         |
| accommodation_facilities | List[int]                      | ❌       | A signed integer number that uniquely identifies an accommodation property facility. Examples of facilities are: Parking, Restaurant, Room service etc.                                                                                                                                                                                             |
| accommodation_types      | List[int]                      | ❌       | A signed integer number that uniquely identifies an accommodation property type. Examples of accommodation types are: Apartment, Hostel, Hotel etc.                                                                                                                                                                                                 |
| airport                  | str                            | ❌       | A three-letter code that uniquely identifies an airport as defined by the International Air Transport Association (IATA).                                                                                                                                                                                                                           |
| brands                   | List[int]                      | ❌       | A signed integer number that uniquely identifies an accommodation brand. Examples of brands are: Radisson Blu, WestCord Hotels, Westin etc.                                                                                                                                                                                                         |
| city                     | int                            | ❌       | A signed integer number that uniquely identifies a city.                                                                                                                                                                                                                                                                                            |
| country                  | str                            | ❌       | A two-letter code that uniquely identifies a country. This code is defined by the ISO 3166-1 alpha-2 standard (ISO2) as described here: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2.                                                                                                                                                           |
| region                   | int                            | ❌       | A signed integer number that uniquely identifies a geographical region. Regions usually define official administrative areas within a country, but may also include multiple countries and in some cases un-official but popular designations for geographical areas. An example of a region that crosses multiple countries is the Alps in Europe. |
| extras                   | List[DetailsInputDtoExtras]    | ❌       | Input parameter to request for additional information about the accommodation property. It should be passed as a JSON array with one or more items.                                                                                                                                                                                                 |
| languages                | List[DetailsInputDtoLanguages] | ❌       | An IETF language tag code that uniquely identifies a supported human language or dialect as described here: https://en.wikipedia.org/wiki/IETF_language_tag. Note that in in demand-api-v3-compatible the whole tag is always lowercase. Examples: "nl" for Dutch/Nederlands or "en-us" for English (US).                                           |
| rows                     | int                            | ❌       | The maximum number of results to return.                                                                                                                                                                                                                                                                                                            |
| page                     | str                            | ❌       | Pagination token used to retrieve the next page of results. Obtained from `next_page`.                                                                                                                                                                                                                                                              |

# DetailsInputDtoExtras

Input parameter to request for additional information about the accommodation property.
It should be passed as a JSON array with one or more items.

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| DESCRIPTION | str  | ✅       | "DESCRIPTION" |
| FACILITIES  | str  | ✅       | "FACILITIES"  |
| PAYMENT     | str  | ✅       | "PAYMENT"     |
| PHOTOS      | str  | ✅       | "PHOTOS"      |
| POLICIES    | str  | ✅       | "POLICIES"    |
| ROOMS       | str  | ✅       | "ROOMS"       |

# DetailsInputDtoLanguages

An IETF language tag code that uniquely identifies a supported human language or dialect as described here:
https://en.wikipedia.org/wiki/IETF_language_tag.

Note that in in demand-api-v3-compatible the whole tag is always lowercase.
Examples: "nl" for Dutch/Nederlands or "en-us" for English (US).

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| AR    | str  | ✅       | "AR"        |
| BG    | str  | ✅       | "BG"        |
| CA    | str  | ✅       | "CA"        |
| CS    | str  | ✅       | "CS"        |
| DA    | str  | ✅       | "DA"        |
| DE    | str  | ✅       | "DE"        |
| EL    | str  | ✅       | "EL"        |
| EN    | str  | ✅       | "EN"        |
| EN_GB | str  | ✅       | "EN_GB"     |
| EN_US | str  | ✅       | "EN_US"     |
| ES    | str  | ✅       | "ES"        |
| ES_AR | str  | ✅       | "ES_AR"     |
| ES_MX | str  | ✅       | "ES_MX"     |
| ET    | str  | ✅       | "ET"        |
| FI    | str  | ✅       | "FI"        |
| FR    | str  | ✅       | "FR"        |
| HE    | str  | ✅       | "HE"        |
| HI    | str  | ✅       | "HI"        |
| HR    | str  | ✅       | "HR"        |
| HU    | str  | ✅       | "HU"        |
| ID    | str  | ✅       | "ID"        |
| IS    | str  | ✅       | "IS"        |
| IT    | str  | ✅       | "IT"        |
| JA    | str  | ✅       | "JA"        |
| KA    | str  | ✅       | "KA"        |
| KO    | str  | ✅       | "KO"        |
| LT    | str  | ✅       | "LT"        |
| LV    | str  | ✅       | "LV"        |
| MS    | str  | ✅       | "MS"        |
| NL    | str  | ✅       | "NL"        |
| NO    | str  | ✅       | "NO"        |
| PL    | str  | ✅       | "PL"        |
| PT_BR | str  | ✅       | "PT_BR"     |
| PT_PT | str  | ✅       | "PT_PT"     |
| RO    | str  | ✅       | "RO"        |
| RU    | str  | ✅       | "RU"        |
| SK    | str  | ✅       | "SK"        |
| SL    | str  | ✅       | "SL"        |
| SR    | str  | ✅       | "SR"        |
| SV    | str  | ✅       | "SV"        |
| TH    | str  | ✅       | "TH"        |
| TL    | str  | ✅       | "TL"        |
| TR    | str  | ✅       | "TR"        |
| UK    | str  | ✅       | "UK"        |
| VI    | str  | ✅       | "VI"        |
| ZH_CN | str  | ✅       | "ZH_CN"     |
| ZH_TW | str  | ✅       | "ZH_TW"     |

<!-- This file was generated by liblab | https://liblab.com/ -->
