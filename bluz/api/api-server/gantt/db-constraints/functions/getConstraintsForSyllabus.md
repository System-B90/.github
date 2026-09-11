[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / getConstraintsForSyllabus

# Function: getConstraintsForSyllabus()

> **getConstraintsForSyllabus**(`syllabusId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:181](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/db-constraints.ts#L181)

Retrieves all constraints for any module or event within a specific syllabus using a single database query.

## Parameters

### syllabusId

`string`

The unique identifier of the syllabus.

## Returns

`Promise`\<`object`[]\>

An array of constraints found.
