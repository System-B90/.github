[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-calendar-snapshot](../../../index.md) / [DbCalendarSnapshot](../index.md) / get

# Variable: get

> `const` **get**: (`snapshotId`, `controller`) => `Promise`\<[`CalendarSnapshot`](../../../../../api-shared/types/type-aliases/CalendarSnapshot.md)\> = `getSnapshot`

Defined in: [ui/src/api-server/db-calendar-snapshot.ts:367](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/db-calendar-snapshot.ts#L367)

Fetches a single snapshot, including its full captured events.

## Parameters

### snapshotId

`string`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`CalendarSnapshot`](../../../../../api-shared/types/type-aliases/CalendarSnapshot.md)\>
