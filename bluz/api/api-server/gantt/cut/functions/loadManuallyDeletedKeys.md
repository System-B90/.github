[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / loadManuallyDeletedKeys

# Function: loadManuallyDeletedKeys()

> **loadManuallyDeletedKeys**(`controller`, `curriculumId`, `week?`): `Promise`\<`Set`\<`string`\>\>

Defined in: [ui/src/api-server/gantt/cut.ts:1001](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/gantt/cut.ts#L1001)

Occurrences a human deleted from the schedule since the cut: archived cut
events whose change log holds a non-gantt archive row. Archives written by
the gantt itself (a reload removal, a pull-back, a week re-cut) do not
count — those occurrences really are gone from the plan, or were never the
user's call.

## Parameters

### controller

[`DatabaseController`](../../../mongo-db-controller/classes/DatabaseController.md)

### curriculumId

`string`

### week?

`DateRange`

Only occurrences dated inside this week, when given.

## Returns

`Promise`\<`Set`\<`string`\>\>

The [occurrenceKey](../../../../api-shared/gantt/reload-diff/functions/occurrenceKey.md)s of the deleted occurrences.
