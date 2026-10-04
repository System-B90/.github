[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / getConstraintsForOwner

# Function: getConstraintsForOwner()

> **getConstraintsForOwner**(`ownerId`, `ownerType`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:31](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/gantt/db-constraints.ts#L31)

Retrieves all constraints owned by a specific Event or Module.
Used to load the dependencies a specific entity has before it can be scheduled.

## Parameters

### ownerId

`string`

The ID of the owner event or module.

### ownerType

[`EntityType`](../type-aliases/EntityType.md)

The entity type ("event" or "module").

## Returns

`Promise`\<`object`[]\>

An array of constraints owned by the entity.
