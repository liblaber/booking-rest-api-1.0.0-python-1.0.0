# KeyCollectionInformationDto

**Properties**

| Name               | Type                      | Required | Description                                                                                                                                                                                                                                |
| :----------------- | :------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| alternate_location | AlternativeKeyLocationDto | ❌       | Alternate location to collect the key of this accommodation property. This is returned if the key to access the property is in another location.                                                                                           |
| checkin_method     | str                       | ❌       | An enumeration that describes the conditions for the checkin process and for collecting the key to access the property. This is typically relevant for non-hotel accommodations (like houses or apartments) without a 24 hours front-desk. |
| key_location       | str                       | ❌       | Location of the key to access this accommodation property.                                                                                                                                                                                 |

<!-- This file was generated by liblab | https://liblab.com/ -->