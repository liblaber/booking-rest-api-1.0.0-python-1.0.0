# BlockAvailabilityInputDto

**Properties**

| Name          | Type                                  | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :------------ | :------------------------------------ | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hotel_ids     | List[int]                             | ✅       | Hotel ID(s) to check availability for.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| checkin       | str                                   | ✅       | The arrival date.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| checkout      | str                                   | ✅       | The departure date. Must be later than (checkin).                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| guest_cc      | str                                   | ✅       | Guest country code. Used to accurately display the best prices and price details for people from that country.                                                                                                                                                                                                                                                                                                                                                                                                   |
| currency      | str                                   | ❌       | Returns the prices in this currency, in addition to the hotel currency.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| extras        | List[BlockAvailabilityInputDtoExtras] | ❌       | The extra items for this request. See the documentation for more details about each extra.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| affiliate_id  | str                                   | ❌       | Application affiliate id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| block_ids     | List[str]                             | ❌       | Return only availability hits with these particular block IDs                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| guest_ip      | str                                   | ❌       | Guest IP address for determining guest country and showing the best price for that user and obeying laws regarding the display of taxes and fees.                                                                                                                                                                                                                                                                                                                                                                |
| guest_qty     | List[int]                             | ❌       | Number of guests for which blocks will be found. The total number of guests is used for calculating city tax charges. It is specified as an array of guest numbers. If you use this parameter and make bookings through the API, you should also set the exact same value in the guest_quantities parameter for the processBooking call, otherwise per-person included charges may result in pricing problems, causing the booking to fail. NOTE: After version 2.6 either this or `room1` needs to be provided. |
| language      | BlockAvailabilityInputDtoLanguage     | ❌       | Specify the language for: block_id, policies, room texts and hotel descriptions. Note: not all text is translated in all languages. Please check the "Possible Values" section of the documentation for the accepted language codes.                                                                                                                                                                                                                                                                             |
| num_rooms     | int                                   | ❌       | Takes a number of rooms to put guests into                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| room1         | List[str]                             | ❌       | Which guests to put in which rooms. Syntax: comma-separated list, `A` for each adult, a number in the range 0..17 for each child.                                                                                                                                                                                                                                                                                                                                                                                |
| user_platform | BlockAvailabilityInputDtoUserPlatform | ❌       | The user's platform.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

# BlockAvailabilityInputDtoExtras

The extra items for this request. See the documentation for more details about each extra.

**Properties**

| Name                     | Type | Required | Description                |
| :----------------------- | :--- | :------- | :------------------------- |
| ADDON_TYPE               | str  | ✅       | "ADDON_TYPE"               |
| NET_PRICE                | str  | ✅       | "NET_PRICE"                |
| RACK_RATES               | str  | ✅       | "RACK_RATES"               |
| MAX_ROOMS_IN_RESERVATION | str  | ✅       | "MAX_ROOMS_IN_RESERVATION" |
| SMOKING_STATUS           | str  | ✅       | "SMOKING_STATUS"           |
| IMPORTANT_INFORMATION    | str  | ✅       | "IMPORTANT_INFORMATION"    |
| ALL_EXTRA_CHARGES        | str  | ✅       | "ALL_EXTRA_CHARGES"        |
| ADDITIONAL_ROOM_INFO     | str  | ✅       | "ADDITIONAL_ROOM_INFO"     |
| GROUP_RECOMMENDATIONS    | str  | ✅       | "GROUP_RECOMMENDATIONS"    |
| ROOM_TYPE_ID             | str  | ✅       | "ROOM_TYPE_ID"             |
| CC_REQUIRED              | str  | ✅       | "CC_REQUIRED"              |
| SHOW_CONDITIONAL_CHARGES | str  | ✅       | "SHOW_CONDITIONAL_CHARGES" |
| POSTCARD_PHOTO           | str  | ✅       | "POSTCARD_PHOTO"           |
| EXTRA_CHARGES            | str  | ✅       | "EXTRA_CHARGES"            |
| PHOTOS                   | str  | ✅       | "PHOTOS"                   |
| INTERNET                 | str  | ✅       | "INTERNET"                 |
| IF_DOMESTIC_NO_CC        | str  | ✅       | "IF_DOMESTIC_NO_CC"        |
| FACILITIES               | str  | ✅       | "FACILITIES"               |
| EXTRA_BEDS               | str  | ✅       | "EXTRA_BEDS"               |
| CANCELLATION_INFO        | str  | ✅       | "CANCELLATION_INFO"        |
| MEALPLANS                | str  | ✅       | "MEALPLANS"                |
| DEAL_LASTM               | str  | ✅       | "DEAL_LASTM"               |
| PAYMENT_TERMS            | str  | ✅       | "PAYMENT_TERMS"            |
| ALL_PRICES               | str  | ✅       | "ALL_PRICES"               |
| BLOCK_PAYMENT_OPTIONS    | str  | ✅       | "BLOCK_PAYMENT_OPTIONS"    |
| MAX_CHILDREN_FREE_AGE    | str  | ✅       | "MAX_CHILDREN_FREE_AGE"    |
| NUMBER_OF_ROOMS_LEFT     | str  | ✅       | "NUMBER_OF_ROOMS_LEFT"     |
| MAX_CHILDREN_FREE        | str  | ✅       | "MAX_CHILDREN_FREE"        |
| POLICIES                 | str  | ✅       | "POLICIES"                 |
| PREPAYMENT_INFO          | str  | ✅       | "PREPAYMENT_INFO"          |
| DEAL_FLASH               | str  | ✅       | "DEAL_FLASH"               |
| IF_NO_CC_ALLOWED         | str  | ✅       | "IF_NO_CC_ALLOWED"         |
| DEAL_SMART               | str  | ✅       | "DEAL_SMART"               |
| ADDONS                   | str  | ✅       | "ADDONS"                   |
| ADDRESS_REQUIRED         | str  | ✅       | "ADDRESS_REQUIRED"         |

# BlockAvailabilityInputDtoLanguage

Specify the language for: block_id, policies, room texts and hotel descriptions.

Note: not all text is translated in all languages.
Please check the "Possible Values" section of the documentation for the accepted language codes.

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

# BlockAvailabilityInputDtoUserPlatform

The user's platform.

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| ANDROID | str  | ✅       | "ANDROID"   |
| DESKTOP | str  | ✅       | "DESKTOP"   |
| IOS     | str  | ✅       | "IOS"       |
| MOBILE  | str  | ✅       | "MOBILE"    |
| TABLET  | str  | ✅       | "TABLET"    |

<!-- This file was generated by liblab | https://liblab.com/ -->
