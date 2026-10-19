[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/constraint](../index.md) / qualifiedEntityName

# Function: qualifiedEntityName()

> **qualifiedEntityName**(`type`, `id`, `state`): `string`

Defined in: [ui/src/api-shared/types/gantt/models/constraint.ts:168](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/models/constraint.ts#L168)

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
