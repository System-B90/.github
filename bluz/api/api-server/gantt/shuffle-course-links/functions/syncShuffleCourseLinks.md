[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/shuffle-course-links](../index.md) / syncShuffleCourseLinks

# Function: syncShuffleCourseLinks()

> **syncShuffleCourseLinks**(`syllabusId`): `Promise`\<`number`\>

Defined in: [ui/src/api-server/gantt/shuffle-course-links.ts:81](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/gantt/shuffle-course-links.ts#L81)

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
