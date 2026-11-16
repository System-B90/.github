[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/schedule-validation/types](../index.md) / RuleCheckEvent

# Type Alias: RuleCheckEvent

> **RuleCheckEvent** = `Pick`\<[`DbEventDocument`](../../../types/event/type-aliases/DbEventDocument.md), `"courses"` \| `"endTime"` \| `"id"` \| `"name"` \| `"rooms"` \| `"startTime"` \| `"subject"` \| `"type"`\> & `Partial`\<`Pick`\<[`DbEventDocument`](../../../types/event/type-aliases/DbEventDocument.md), `"ganttCurriculumId"` \| `"ganttEventId"` \| `"ganttOccurrenceDate"` \| `"instructors"` \| `"lecturers"` \| `"locked"` \| `"notes"` \| `"required"` \| `"splitAcrossBreaks"`\>\> & `object`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:14](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/api-shared/schedule-validation/types.ts#L14)

The event fields the checks read. `startTime`/`endTime` as stored (Date or ISO).

## Type Declaration

### hidden?

> `optional` **hidden?**: `boolean`

### parked?

> `optional` **parked?**: `boolean`
