[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / getConstraintsForSyllabus

# Function: getConstraintsForSyllabus()

> **getConstraintsForSyllabus**(`syllabusId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:230](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-server/gantt/db-constraints.ts#L230)

Retrieves all constraints for any module or event within a specific syllabus using a single database query.

## Parameters

### syllabusId

`string`

The unique identifier of the syllabus.

## Returns

`Promise`\<`object`[]\>

An array of constraints found.
