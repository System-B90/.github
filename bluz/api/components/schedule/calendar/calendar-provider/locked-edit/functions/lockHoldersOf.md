[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar-provider/locked-edit](../index.md) / lockHoldersOf

# Function: lockHoldersOf()

> **lockHoldersOf**(`eventIds`, `eventLocks`): `string`[]

Defined in: [ui/src/components/schedule/calendar/calendar-provider/locked-edit.ts:16](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/schedule/calendar/calendar-provider/locked-edit.ts#L16)

Display names of the other users currently editing any of the events,
de-duplicated in first-seen order.

## Parameters

### eventIds

`Iterable`\<`string`\>

The events about to be edited.

### eventLocks

`Record`\<[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md), [`EventLockMessage`](../../../../../../api-shared/types/type-aliases/EventLockMessage.md) \| `undefined`\>

Live locks held by *other* users (own locks are never tracked).

## Returns

`string`[]
