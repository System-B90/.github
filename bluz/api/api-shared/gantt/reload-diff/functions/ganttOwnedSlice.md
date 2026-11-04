[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/reload-diff](../index.md) / ganttOwnedSlice

# Function: ganttOwnedSlice()

> **ganttOwnedSlice**(`event`, `fields?`): `Record`\<`string`, `unknown`\>

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:70](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/gantt/reload-diff.ts#L70)

Project a document down to the given (gantt-owned) fields only.

## Parameters

### event

[`DbEventDocument`](../../../types/event/type-aliases/DbEventDocument.md)

### fields?

readonly (`"id"` \| `"name"` \| `"type"` \| `"instructors"` \| `"lecturers"` \| `"subject"` \| `"hiveModule"` \| `"hiveLesson"` \| `"startTime"` \| `"endTime"` \| `"courses"` \| `"rooms"` \| `"tags"` \| `"notes"` \| `"locked"` \| `"hidden"` \| `"required"` \| `"personalTalk"` \| `"studentName"` \| `"parked"` \| `"restoredAfterDelete"` \| `"splitAcrossBreaks"` \| `"color"` \| `"fake"` \| `"ganttEventId"` \| `"ganttOccurrenceDate"` \| `"ganttCurriculumId"` \| `"weekTemplateId"` \| `"updatedAt"` \| `"archived"`)[] = `GANTT_OWNED_FIELDS`

## Returns

`Record`\<`string`, `unknown`\>
