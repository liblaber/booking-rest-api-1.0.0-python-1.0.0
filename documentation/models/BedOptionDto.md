# BedOptionDto

Lists all possible bedding options for this room or apartment.

**Properties**

| Name               | Type                      | Required | Description                                                                                  |
| :----------------- | :------------------------ | :------- | :------------------------------------------------------------------------------------------- |
| bed_configurations | List[BedConfigurationDto] | ❌       | Lists all alternative bed configurations that are supported.                                 |
| has_bathroom       | bool                      | ❌       | Flags if this area includes its own bathroom.                                                |
| is_bedroom         | bool                      | ❌       | Flags if this area is marked as a bedroom, otherwise, it should be considered a living room. |

<!-- This file was generated by liblab | https://liblab.com/ -->