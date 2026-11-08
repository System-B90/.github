[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/shuffle-course-links](../index.md) / syncShuffleCourseLinks

# Function: syncShuffleCourseLinks()

> **syncShuffleCourseLinks**(`syllabusId`): `Promise`\<`number`\>

Defined in: [ui/src/api-server/gantt/shuffle-course-links.ts:81](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/gantt/shuffle-course-links.ts#L81)

After a syllabus save: relinks its shuffles' courses in every current
iteration cut from a curriculum that holds it. Never throws — the save it
follows has already committed.

## Parameters

### syllabusId

`string`

The syllabus just saved.

## Returns

`Promise`\<`number`\>

How many courses were relinked.
