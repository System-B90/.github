[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/reload-diff](../index.md) / isDeletedBreak

# Function: isDeletedBreak()

> **isDeletedBreak**(`document`, `manuallyDeletedKeys`): `boolean`

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:47](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/gantt/reload-diff.ts#L47)

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
