[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/settings/hive-integration](../index.md) / HiveIntegrationSettings

# Type Alias: HiveIntegrationSettings

> **HiveIntegrationSettings** = `object`

Defined in: [ui/src/api-shared/types/settings/hive-integration.ts:17](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/settings/hive-integration.ts#L17)

## Properties

### calendarFile?

> `optional` **calendarFile?**: `string`

Defined in: [ui/src/api-shared/types/settings/hive-integration.ts:26](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/settings/hive-integration.ts#L26)

Where the `hive-feed` sidecar writes the ICS feed, relative to the
directory it shares with Hive (`HIVE_CALENDAR_DIRS_PATH`). The directory
itself is a bind mount, fixed when the container starts, so only the
path inside it is editable here. Unset ⇒ the sidecar's own
`HIVE_CALENDAR_FILE`, else [DEFAULT\_HIVE\_CALENDAR\_FILE](../variables/DEFAULT_HIVE_CALENDAR_FILE.md).

***

### feedWindowHours?

> `optional` **feedWindowHours?**: `number`

Defined in: [ui/src/api-shared/types/settings/hive-integration.ts:33](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/settings/hive-integration.ts#L33)

How far the ICS feed reaches, in hours, before the start and after the
end of the current day (Israel time). Hive deletes every Bluz event the
file no longer carries, so this is also what Hive's schedule keeps.
Unset ⇒ [DEFAULT\_HIVE\_FEED\_WINDOW\_HOURS](../variables/DEFAULT_HIVE_FEED_WINDOW_HOURS.md).

***

### lessonDriver

> **lessonDriver**: [`HiveLessonDriver`](../enumerations/HiveLessonDriver.md)

Defined in: [ui/src/api-shared/types/settings/hive-integration.ts:18](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/settings/hive-integration.ts#L18)
