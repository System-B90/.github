[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / updateConstraint

# Function: updateConstraint()

> **updateConstraint**(`constraintId`, `newValues`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:166](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/gantt/db-constraints.ts#L166)

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
