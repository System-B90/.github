[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / updateConstraint

# Function: updateConstraint()

> **updateConstraint**(`constraintId`, `newValues`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:166](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/gantt/db-constraints.ts#L166)

Updates an existing constraint with new values.

## Parameters

### constraintId

`string`

The UUID of the constraint to update.

### newValues

`Partial`\<*typeof* `ganttConstraintsSchema.$inferInsert`\>

The partial payload of values to update.

## Returns

`Promise`\<`object`[]\>

The updated constraint record.
