[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / constraintInsertFromPayload

# Function: constraintInsertFromPayload()

> **constraintInsertFromPayload**(`body`): `object`

Defined in: [ui/src/api-server/gantt/db-constraints.ts:86](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/gantt/db-constraints.ts#L86)

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
