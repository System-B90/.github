[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / deleteConstraint

# Function: deleteConstraint()

> **deleteConstraint**(`constraintId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:153](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-server/gantt/db-constraints.ts#L153)

Deletes a constraint from the database by its identifier.

## Parameters

### constraintId

`string`

The UUID of the constraint to delete.

## Returns

`Promise`\<`object`[]\>

The deleted constraint record.
