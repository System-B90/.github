[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/reload-diff](../index.md) / isDeletedBreak

# Function: isDeletedBreak()

> **isDeletedBreak**(`document`, `manuallyDeletedKeys`): `boolean`

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:47](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/gantt/reload-diff.ts#L47)

Whether a planned occurrence is a break a human deleted from the schedule.
Other deleted occurrences come back parked for the user to place; a parked
break has nothing to hand back, so a deleted break stays deleted.

## Parameters

### document

[`DbEventDocument`](../../../types/event/type-aliases/DbEventDocument.md)

### manuallyDeletedKeys

`ReadonlySet`\<`string`\>

## Returns

`boolean`
