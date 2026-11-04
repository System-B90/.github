[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / deleteConstraint

# Function: deleteConstraint()

> **deleteConstraint**(`constraintId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:184](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/db-constraints.ts#L184)

Deletes a constraint from the database by its identifier.

## Parameters

### constraintId

`string`

The UUID of the constraint to delete.

## Returns

`Promise`\<`object`[]\>

The deleted constraint record.
