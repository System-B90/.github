[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/settings/hive-integration](../index.md) / HiveLessonDriver

# Enumeration: HiveLessonDriver

Defined in: [ui/src/api-shared/types/settings/hive-integration.ts:7](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/settings/hive-integration.ts#L7)

Who opens Hive lessons when a Bluz event goes live. One value, so the two
paths can never run together and double-assign a class.

## Enumeration Members

### ACTIVATOR

> **ACTIVATOR**: `"activator"`

Defined in: [ui/src/api-shared/types/settings/hive-integration.ts:9](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/settings/hive-integration.ts#L9)

Bluz's own 30s activator calls `classes/{id}/lesson/` (the default).

***

### ICS\_FEED

> **ICS\_FEED**: `"icsFeed"`

Defined in: [ui/src/api-shared/types/settings/hive-integration.ts:14](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/settings/hive-integration.ts#L14)

Bluz publishes its schedule as ICS for Hive's external schedule mode
and Hive's `update_schedule` task assigns the lessons itself.
