[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / StudentEventWire

# Type Alias: StudentEventWire

> **StudentEventWire** = `Omit`\<[`StudentEvent`](StudentEvent.md), `"courses"` \| `"relatedCourses"` \| `"rooms"`\> & `object`

Defined in: [ui/src/api-shared/types/student-view.ts:56](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/student-view.ts#L56)

Wire form of `StudentEvent`. Course and room names are shared by most of a
day's events, and `relatedCourses` can span a whole course tree, so each
name is sent once and events reference it by position:
- `rooms` indexes `ApiStudentScheduleGetResponse.roomNames`.
- `courses` / `relatedCourses` index `courseGroups`, whose entries index
  `courseNames`. Events with the same course set share one group.

Indices are positions in this one response only — never course or room ids.

## Type Declaration

### courses

> **courses**: `number`

### relatedCourses

> **relatedCourses**: `number`

### rooms

> **rooms**: `number`[]
