# GuestsInputDto

The guest details for the request.

**Properties**

| Name             | Type                     | Required | Description                              |
| :--------------- | :----------------------- | :------- | :--------------------------------------- |
| number_of_adults | int                      | ✅       | The number of adults for the search.     |
| number_of_rooms  | int                      | ✅       | The number of rooms needed.              |
| allocation       | List[AllocationInputDto] | ❌       | The exact allocation of guests to rooms. |
| children         | List[int]                | ❌       | Array with the children ages.            |

<!-- This file was generated by liblab | https://liblab.com/ -->
