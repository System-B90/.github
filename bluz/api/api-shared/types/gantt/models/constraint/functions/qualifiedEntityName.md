[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/constraint](../index.md) / qualifiedEntityName

# Function: qualifiedEntityName()

> **qualifiedEntityName**(`type`, `id`, `state`): `string`

Defined in: [ui/src/api-shared/types/gantt/models/constraint.ts:141](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/gantt/models/constraint.ts#L141)

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
