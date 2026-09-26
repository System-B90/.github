[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event-history](../../../index.md) / [DbEventHistory](../index.md) / forEvents

# Variable: forEvents

> `const` **forEvents**: (`eventIds`, `controller`) => `Promise`\<`Map`\<`string`, [`EventHistoryEntry`](../../../../../api-shared/types/event-history/type-aliases/EventHistoryEntry.md)[]\>\> = `listForEvents`

Defined in: [ui/src/api-server/db-event-history.ts:230](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/db-event-history.ts#L230)

Logs of many events at once, grouped by event id. Used by the gantt reload to
classify a whole cut in one query instead of N.

## Parameters

### eventIds

`string`[]

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<`Map`\<`string`, [`EventHistoryEntry`](../../../../../api-shared/types/event-history/type-aliases/EventHistoryEntry.md)[]\>\>
