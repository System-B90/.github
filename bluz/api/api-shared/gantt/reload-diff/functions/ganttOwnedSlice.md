[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/reload-diff](../index.md) / ganttOwnedSlice

# Function: ganttOwnedSlice()

> **ganttOwnedSlice**(`event`, `fields?`): `Record`\<`string`, `unknown`\>

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:70](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/gantt/reload-diff.ts#L70)

Project a document down to the given (gantt-owned) fields only.

## Parameters

### event

[`DbEventDocument`](../../../types/event/type-aliases/DbEventDocument.md)

### fields?

readonly (`"id"` \| `"name"` \| `"type"` \| `"instructors"` \| `"lecturers"` \| `"subject"` \| `"hiveModule"` \| `"hiveLesson"` \| `"startTime"` \| `"endTime"` \| `"courses"` \| `"rooms"` \| `"tags"` \| `"notes"` \| `"locked"` \| `"hidden"` \| `"required"` \| `"personalTalk"` \| `"studentName"` \| `"parked"` \| `"restoredAfterDelete"` \| `"splitAcrossBreaks"` \| `"color"` \| `"fake"` \| `"ganttEventId"` \| `"ganttOccurrenceDate"` \| `"ganttCurriculumId"` \| `"weekTemplateId"` \| `"updatedAt"` \| `"archived"`)[] = `GANTT_OWNED_FIELDS`

## Returns

`Record`\<`string`, `unknown`\>
