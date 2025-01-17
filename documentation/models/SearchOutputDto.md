# SearchOutputDto

**Properties**

| Name          | Type               | Required | Description                                                                                                                                                         |
| :------------ | :----------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| id\_          | int                | ❌       | A signed integer number that uniquely identifies an accommodation property.                                                                                         |
| currency      | str                | ❌       | A three-letter code that uniquely identifies a monetary currency as defined by the ISO 4217 standard.                                                               |
| deep_link_url | str                | ❌       | Deep link mobile app URL.                                                                                                                                           |
| url           | str                | ❌       | Internet address for the property page on Booking.com.                                                                                                              |
| price         | PriceDataDtoDouble | ❌       | The price components of this product or selection of products. 'base' and 'extra_charges' are returned only when explicitly requested (via 'extras=extra_charges'). |
| products      | List[ProductDto]   | ❌       |                                                                                                                                                                     |

<!-- This file was generated by liblab | https://liblab.com/ -->
