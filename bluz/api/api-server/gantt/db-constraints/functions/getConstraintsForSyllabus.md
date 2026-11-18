[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / getConstraintsForSyllabus

# Function: getConstraintsForSyllabus()

> **getConstraintsForSyllabus**(`syllabusId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:264](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-server/gantt/db-constraints.ts#L264)

Retrieves all constraints for any module or event within a specific syllabus using a single database query.

## Parameters

### syllabusId

`string`

The unique identifier of the syllabus.

## Returns

`Promise`\<`object`[]\>

An array of constraints found.
