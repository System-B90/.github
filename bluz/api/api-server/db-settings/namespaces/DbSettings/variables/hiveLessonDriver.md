[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-settings](../../../index.md) / [DbSettings](../index.md) / hiveLessonDriver

# Variable: hiveLessonDriver

> `const` **hiveLessonDriver**: (`controller`) => `Promise`\<[`HiveLessonDriver`](../../../../../api-shared/types/settings/hive-integration/enumerations/HiveLessonDriver.md)\> = `getHiveLessonDriver`

Defined in: [ui/src/api-server/db-settings.ts:153](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/db-settings.ts#L153)

Which path opens Hive lessons for this iteration. A missing or corrupt
setting falls back to the activator, i.e. behaviour before the setting.

## Parameters

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`HiveLessonDriver`](../../../../../api-shared/types/settings/hive-integration/enumerations/HiveLessonDriver.md)\>
