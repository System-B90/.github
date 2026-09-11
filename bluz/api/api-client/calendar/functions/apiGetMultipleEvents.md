[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar](../index.md) / apiGetMultipleEvents

# Function: apiGetMultipleEvents()

> **apiGetMultipleEvents**(`eventIds`, `iterationId?`): `Promise`\<`Partial`\<`Record`\<`string`, [`Event`](../../../api-shared/types/event/type-aliases/Event.md)\>\>\>

Defined in: [ui/src/api-client/calendar.ts:55](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/calendar.ts#L55)

Fetches several events by id in one round-trip. The route
(`app/api/event/route.ts`) filters out malformed ids and silently omits
ids it can't find, so the response can carry fewer keys than
`eventIds` — the return type is `Partial<...>` precisely so every
caller has to handle a missing id instead of the old `Record<EventId,
Event>` signature promising a complete map it couldn't guarantee.

## Parameters

### eventIds

`string`[]

### iterationId?

`string`

## Returns

`Promise`\<`Partial`\<`Record`\<`string`, [`Event`](../../../api-shared/types/event/type-aliases/Event.md)\>\>\>
