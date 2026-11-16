[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-calendar-snapshot](../../../index.md) / [DbCalendarSnapshot](../index.md) / get

# Variable: get

> `const` **get**: (`snapshotId`, `controller`) => `Promise`\<[`CalendarSnapshot`](../../../../../api-shared/types/type-aliases/CalendarSnapshot.md)\> = `getSnapshot`

Defined in: [ui/src/api-server/db-calendar-snapshot.ts:367](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-server/db-calendar-snapshot.ts#L367)

Fetches a single snapshot, including its full captured events.

## Parameters

### snapshotId

`string`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`CalendarSnapshot`](../../../../../api-shared/types/type-aliases/CalendarSnapshot.md)\>
