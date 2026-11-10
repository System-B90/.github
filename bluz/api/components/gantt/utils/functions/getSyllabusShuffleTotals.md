[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/utils](../index.md) / getSyllabusShuffleTotals

# Function: getSyllabusShuffleTotals()

> **getSyllabusShuffleTotals**(`syllabus`, `fieldName`, `state`, `occurrenceCtx?`): `Record`\<`string`, `number`\> \| `null`

Defined in: [ui/src/components/gantt/utils.tsx:255](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/utils.tsx#L255)

Per-shuffle sums of an event field across a whole syllabus, or null when
neither the syllabus nor its modules/events are shuffle-tagged.

## Parameters

### syllabus

[`GanttSyllabus`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md)

### fieldName

`NumberFieldKeys`\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)\>

### state

[`NormalizedStore`](../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

### occurrenceCtx?

[`RecurrenceOccurrenceContext`](../type-aliases/RecurrenceOccurrenceContext.md)

## Returns

`Record`\<`string`, `number`\> \| `null`
