# HotelsInputDto

**Properties**

| Name      | Type                       | Required | Description                                                                                                                                  |
| :-------- | :------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| hotel_ids | List[int]                  | ❌       | A list of up to 1000 hotel ids.                                                                                                              |
| language  | HotelsInputDtoLanguage     | ❌       | The language code to return the results in. Please check the "Possible Values" section of the documentation for the accepted language codes. |
| extras    | List[HotelsInputDtoExtras] | ❌       | Returns extra bits of information about hotels.                                                                                              |
| offset    | int                        | ❌       | The number of rows to offset the results by. NOTE: this needs to be 0 or a multiple of 100.                                                  |
| rows      | int                        | ❌       | The maximum number of rows to return. NOTE: this needs to be a multiple of 100.                                                              |

# HotelsInputDtoLanguage

The language code to return the results in.
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

# HotelsInputDtoExtras

Returns extra bits of information about hotels.

**Properties**

| Name                | Type | Required | Description           |
| :------------------ | :--- | :------- | :-------------------- |
| HOTEL_INFO          | str  | ✅       | "HOTEL_INFO"          |
| ROOM_INFO           | str  | ✅       | "ROOM_INFO"           |
| KEY_COLLECTION_INFO | str  | ✅       | "KEY_COLLECTION_INFO" |
| HOTEL_FACILITIES    | str  | ✅       | "HOTEL_FACILITIES"    |
| HOTEL_PHOTOS        | str  | ✅       | "HOTEL_PHOTOS"        |
| HOTEL_DESCRIPTION   | str  | ✅       | "HOTEL_DESCRIPTION"   |

<!-- This file was generated by liblab | https://liblab.com/ -->