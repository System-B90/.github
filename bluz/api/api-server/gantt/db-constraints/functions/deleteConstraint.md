[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / deleteConstraint

# Function: deleteConstraint()

> **deleteConstraint**(`constraintId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:104](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/gantt/db-constraints.ts#L104)

Deletes a constraint from the database by its identifier.

## Parameters

### constraintId

`string`

The UUID of the constraint to delete.

## Returns

`Promise`\<`object`[]\>

The deleted constraint record.
