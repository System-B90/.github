[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/settings/hive-integration](../index.md) / HiveLessonDriver

# Enumeration: HiveLessonDriver

Defined in: [ui/src/api-shared/types/settings/hive-integration.ts:7](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/settings/hive-integration.ts#L7)

Who opens Hive lessons when a Bluz event goes live. One value, so the two
paths can never run together and double-assign a class.

## Enumeration Members

### ACTIVATOR

> **ACTIVATOR**: `"activator"`

Defined in: [ui/src/api-shared/types/settings/hive-integration.ts:9](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/settings/hive-integration.ts#L9)

Bluz's own 30s activator calls `classes/{id}/lesson/` (the default).

***

### ICS\_FEED

> **ICS\_FEED**: `"icsFeed"`

Defined in: [ui/src/api-shared/types/settings/hive-integration.ts:14](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/settings/hive-integration.ts#L14)

Bluz publishes its schedule as ICS for Hive's external schedule mode
and Hive's `update_schedule` task assigns the lessons itself.
