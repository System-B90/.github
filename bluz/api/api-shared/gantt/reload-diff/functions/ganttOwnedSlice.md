[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/reload-diff](../index.md) / ganttOwnedSlice

# Function: ganttOwnedSlice()

> **ganttOwnedSlice**(`event`, `fields?`): `Record`\<`string`, `unknown`\>

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:70](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/gantt/reload-diff.ts#L70)

Project a document down to the given (gantt-owned) fields only.

## Parameters

### event

[`DbEventDocument`](../../../types/event/type-aliases/DbEventDocument.md)

### fields?

readonly (`"id"` \| `"name"` \| `"type"` \| `"instructors"` \| `"lecturers"` \| `"subject"` \| `"hiveModule"` \| `"hiveLesson"` \| `"startTime"` \| `"endTime"` \| `"courses"` \| `"rooms"` \| `"tags"` \| `"notes"` \| `"locked"` \| `"hidden"` \| `"required"` \| `"personalTalk"` \| `"studentName"` \| `"parked"` \| `"restoredAfterDelete"` \| `"splitAcrossBreaks"` \| `"color"` \| `"fake"` \| `"ganttEventId"` \| `"ganttOccurrenceDate"` \| `"ganttCurriculumId"` \| `"weekTemplateId"` \| `"updatedAt"` \| `"archived"`)[] = `GANTT_OWNED_FIELDS`

## Returns

`Record`\<`string`, `unknown`\>
