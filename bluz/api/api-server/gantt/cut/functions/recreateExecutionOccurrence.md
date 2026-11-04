[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / recreateExecutionOccurrence

# Function: recreateExecutionOccurrence()

> **recreateExecutionOccurrence**(`curriculumId`, `ganttEventId`, `occurrenceDate`): `Promise`\<[`RecreateOccurrenceOutcome`](../type-aliases/RecreateOccurrenceOutcome.md)\>

Defined in: [ui/src/api-server/gantt/cut.ts:2073](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/gantt/cut.ts#L2073)

Re-create the schedule event(s) for one gantt-event occurrence that was cut
and later deleted from the schedule (#682). Re-runs the full materialization
(same computation as a cut/reload) and inserts only the document(s) matching
`(ganttEventId, occurrenceDate)`, so the recreated event matches the gantt
plan exactly. Refuses when a live event already occupies that occurrence —
the caller should delete it first if it wants to replace it.

## Parameters

### curriculumId

`string`

### ganttEventId

`string`

### occurrenceDate

`string`

## Returns

`Promise`\<[`RecreateOccurrenceOutcome`](../type-aliases/RecreateOccurrenceOutcome.md)\>
