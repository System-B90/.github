[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / getConstraintsForSyllabus

# Function: getConstraintsForSyllabus()

> **getConstraintsForSyllabus**(`syllabusId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:264](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/gantt/db-constraints.ts#L264)

Retrieves all constraints for any module or event within a specific syllabus using a single database query.

## Parameters

### syllabusId

`string`

The unique identifier of the syllabus.

## Returns

`Promise`\<`object`[]\>

An array of constraints found.
