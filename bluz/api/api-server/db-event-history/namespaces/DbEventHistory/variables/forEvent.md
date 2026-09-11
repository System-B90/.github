[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event-history](../../../index.md) / [DbEventHistory](../index.md) / forEvent

# Variable: forEvent

> `const` **forEvent**: (`eventId`, `controller`) => `Promise`\<[`EventHistoryEntry`](../../../../../api-shared/types/event-history/type-aliases/EventHistoryEntry.md)[]\> = `listForEvent`

Defined in: [ui/src/api-server/db-event-history.ts:229](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/db-event-history.ts#L229)

Full log of one event, newest first.

## Parameters

### eventId

`string`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`EventHistoryEntry`](../../../../../api-shared/types/event-history/type-aliases/EventHistoryEntry.md)[]\>
