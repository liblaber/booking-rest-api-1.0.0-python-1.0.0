# CancellationDto

The cancellation policy for this product.

**Properties**

| Name                    | Type | Required | Description                                                      |
| :---------------------- | :--- | :------- | :--------------------------------------------------------------- |
| free_cancellation_until | str  | ❌       | Until when the order for this product can be cancelled for free. |
| type\_                  | Type | ❌       | The cancellation scheme supported by this product.               |

# Type

The cancellation scheme supported by this product.

**Properties**

| Name               | Type | Required | Description          |
| :----------------- | :--- | :------- | :------------------- |
| FREE_CANCELLATION  | str  | ✅       | "FREE_CANCELLATION"  |
| NON_REFUNDABLE     | str  | ✅       | "NON_REFUNDABLE"     |
| SPECIAL_CONDITIONS | str  | ✅       | "SPECIAL_CONDITIONS" |

<!-- This file was generated by liblab | https://liblab.com/ -->