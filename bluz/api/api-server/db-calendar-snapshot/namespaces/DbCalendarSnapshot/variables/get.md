[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-calendar-snapshot](../../../index.md) / [DbCalendarSnapshot](../index.md) / get

# Variable: get

> `const` **get**: (`snapshotId`, `controller`) => `Promise`\<[`CalendarSnapshot`](../../../../../api-shared/types/type-aliases/CalendarSnapshot.md)\> = `getSnapshot`

Defined in: [ui/src/api-server/db-calendar-snapshot.ts:282](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/db-calendar-snapshot.ts#L282)

Fetches a single snapshot, including its full captured events.

## Parameters

### snapshotId

`string`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`CalendarSnapshot`](../../../../../api-shared/types/type-aliases/CalendarSnapshot.md)\>
