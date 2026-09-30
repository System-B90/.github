[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / updateConstraint

# Function: updateConstraint()

> **updateConstraint**(`constraintId`, `newValues`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:136](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/gantt/db-constraints.ts#L136)

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
