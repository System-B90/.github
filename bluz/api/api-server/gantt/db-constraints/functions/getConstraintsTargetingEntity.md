[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / getConstraintsTargetingEntity

# Function: getConstraintsTargetingEntity()

> **getConstraintsTargetingEntity**(`targetId`, `targetType`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:54](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/gantt/db-constraints.ts#L54)

Retrieves constraints targeting a specific Event or Module.
Useful for cascade checking, highlighting dependencies in the UI, or cyclic dependency resolution.

## Parameters

### targetId

`string`

The ID of the target event or module.

### targetType

[`EntityType`](../type-aliases/EntityType.md)

The entity type ("event" or "module").

## Returns

`Promise`\<`object`[]\>

An array of constraints targeting the entity.
