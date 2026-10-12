[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / getConstraintsForCurriculum

# Function: getConstraintsForCurriculum()

> **getConstraintsForCurriculum**(`curriculumId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:173](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-server/gantt/db-constraints.ts#L173)

Retrieves all constraints associated with a specific curriculum.
Resolves constraints owned by any modules or events mapped to the curriculum.

## Parameters

### curriculumId

`string`

The curriculum identifier.

## Returns

`Promise`\<`object`[]\>

An array of constraints for the curriculum.
