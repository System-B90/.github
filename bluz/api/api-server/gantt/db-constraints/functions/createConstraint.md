[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / createConstraint

# Function: createConstraint()

> **createConstraint**(`data`): `Promise`\<\{ `allowedDays`: `number`[] \| `null`; `createdAt`: `Date`; `forbiddenDays`: `number`[] \| `null`; `id`: `string`; `maxDelayDays`: `number` \| `null`; `minDelayDays`: `number` \| `null`; `ownerEventId`: `string` \| `null`; `ownerModuleId`: `string` \| `null`; `relation`: `"after"` \| `"before"` \| `null`; `targetEventId`: `string` \| `null`; `targetModuleId`: `string` \| `null`; `type`: `"RELATIONAL"` \| `"TEMPORAL"`; `updatedAt`: `Date`; \}\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:73](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/gantt/db-constraints.ts#L73)

Creates a new constraint in the database.

## Parameters

### data

The constraint insert payload.

#### allowedDays?

`number`[] \| `null`

#### createdAt?

`Date`

#### forbiddenDays?

`number`[] \| `null`

#### id

`string`

#### maxDelayDays?

`number` \| `null`

#### minDelayDays?

`number` \| `null`

#### ownerEventId?

`string` \| `null`

#### ownerModuleId?

`string` \| `null`

#### relation?

`"after"` \| `"before"` \| `null`

#### targetEventId?

`string` \| `null`

#### targetModuleId?

`string` \| `null`

#### type

`"RELATIONAL"` \| `"TEMPORAL"`

#### updatedAt?

`Date`

## Returns

`Promise`\<\{ `allowedDays`: `number`[] \| `null`; `createdAt`: `Date`; `forbiddenDays`: `number`[] \| `null`; `id`: `string`; `maxDelayDays`: `number` \| `null`; `minDelayDays`: `number` \| `null`; `ownerEventId`: `string` \| `null`; `ownerModuleId`: `string` \| `null`; `relation`: `"after"` \| `"before"` \| `null`; `targetEventId`: `string` \| `null`; `targetModuleId`: `string` \| `null`; `type`: `"RELATIONAL"` \| `"TEMPORAL"`; `updatedAt`: `Date`; \}\>

The created constraint record.
