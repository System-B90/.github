[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / constraintInsertFromPayload

# Function: constraintInsertFromPayload()

> **constraintInsertFromPayload**(`body`): `object`

Defined in: [ui/src/api-server/gantt/db-constraints.ts:89](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/db-constraints.ts#L89)

Validates a client (or assistant) constraint payload and maps it to the
row shape. Shared by the REST route and the AI tool so both enforce the
same owner/target rules.

## Parameters

### body

[`CreateConstraintPayload`](../../../../api-shared/types/gantt/create-payloads/type-aliases/CreateConstraintPayload.md)

## Returns

`object`

### allowedDays?

> `optional` **allowedDays?**: `number`[] \| `null`

### createdAt?

> `optional` **createdAt?**: `Date`

### forbiddenDays?

> `optional` **forbiddenDays?**: `number`[] \| `null`

### id

> **id**: `string`

### maxDelayDays?

> `optional` **maxDelayDays?**: `number` \| `null`

### minDelayDays?

> `optional` **minDelayDays?**: `number` \| `null`

### ownerEventId?

> `optional` **ownerEventId?**: `string` \| `null`

### ownerModuleId?

> `optional` **ownerModuleId?**: `string` \| `null`

### relation?

> `optional` **relation?**: `"after"` \| `"before"` \| `null`

### targetEventId?

> `optional` **targetEventId?**: `string` \| `null`

### targetModuleId?

> `optional` **targetModuleId?**: `string` \| `null`

### type

> **type**: `"RELATIONAL"` \| `"TEMPORAL"`

### updatedAt?

> `optional` **updatedAt?**: `Date`
