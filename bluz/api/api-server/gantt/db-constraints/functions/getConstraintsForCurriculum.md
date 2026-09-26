[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / getConstraintsForCurriculum

# Function: getConstraintsForCurriculum()

> **getConstraintsForCurriculum**(`curriculumId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:124](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/gantt/db-constraints.ts#L124)

Retrieves all constraints associated with a specific curriculum.
Resolves constraints owned by any modules or events mapped to the curriculum.

## Parameters

### curriculumId

`string`

The curriculum identifier.

## Returns

`Promise`\<`object`[]\>

An array of constraints for the curriculum.
