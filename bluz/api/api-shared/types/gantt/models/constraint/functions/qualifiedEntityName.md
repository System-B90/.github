[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/constraint](../index.md) / qualifiedEntityName

# Function: qualifiedEntityName()

> **qualifiedEntityName**(`type`, `id`, `state`): `string`

Defined in: [ui/src/api-shared/types/gantt/models/constraint.ts:181](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-shared/types/gantt/models/constraint.ts#L181)

Fully qualified name of a constraint endpoint: "syllabus › module" for a
module, "syllabus › module › event" for an event. Missing ancestors are
dropped; a missing entity itself reads as "not found".

## Parameters

### type

[`EntityType`](../type-aliases/EntityType.md)

### id

`string`

### state

[`ConstraintDisplayState`](../type-aliases/ConstraintDisplayState.md)

## Returns

`string`
