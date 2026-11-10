[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event-history](../../../index.md) / [DbEventHistory](../index.md) / forEvent

# Variable: forEvent

> `const` **forEvent**: (`eventId`, `controller`) => `Promise`\<[`EventHistoryEntry`](../../../../../api-shared/types/event-history/type-aliases/EventHistoryEntry.md)[]\> = `listForEvent`

Defined in: [ui/src/api-server/db-event-history.ts:246](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/db-event-history.ts#L246)

Full log of one event, newest first.

## Parameters

### eventId

`string`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`EventHistoryEntry`](../../../../../api-shared/types/event-history/type-aliases/EventHistoryEntry.md)[]\>
