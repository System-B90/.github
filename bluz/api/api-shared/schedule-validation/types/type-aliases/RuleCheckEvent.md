[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/schedule-validation/types](../index.md) / RuleCheckEvent

# Type Alias: RuleCheckEvent

> **RuleCheckEvent** = `Pick`\<[`DbEventDocument`](../../../types/event/type-aliases/DbEventDocument.md), `"courses"` \| `"endTime"` \| `"id"` \| `"name"` \| `"rooms"` \| `"startTime"` \| `"subject"` \| `"type"`\> & `Partial`\<`Pick`\<[`DbEventDocument`](../../../types/event/type-aliases/DbEventDocument.md), `"ganttCurriculumId"` \| `"ganttEventId"` \| `"ganttOccurrenceDate"` \| `"instructors"` \| `"lecturers"` \| `"locked"` \| `"notes"` \| `"required"` \| `"splitAcrossBreaks"`\>\> & `object`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:14](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/schedule-validation/types.ts#L14)

The event fields the checks read. `startTime`/`endTime` as stored (Date or ISO).

## Type Declaration

### hidden?

> `optional` **hidden?**: `boolean`

### parked?

> `optional` **parked?**: `boolean`
