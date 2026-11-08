[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / getConstraintsForCurriculum

# Function: getConstraintsForCurriculum()

> **getConstraintsForCurriculum**(`curriculumId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:206](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/gantt/db-constraints.ts#L206)

Retrieves all constraints associated with a specific curriculum.
Resolves constraints owned by any modules or events mapped to the curriculum.

## Parameters

### curriculumId

`string`

The curriculum identifier.

## Returns

`Promise`\<`object`[]\>

An array of constraints for the curriculum.
