[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / createConstraint

# Function: createConstraint()

> **createConstraint**(`data`): `Promise`\<\{ `allowedDays`: `number`[] \| `null`; `createdAt`: `Date`; `forbiddenDays`: `number`[] \| `null`; `id`: `string`; `maxDelayDays`: `number` \| `null`; `minDelayDays`: `number` \| `null`; `ownerEventId`: `string` \| `null`; `ownerModuleId`: `string` \| `null`; `relation`: `"after"` \| `"before"` \| `null`; `targetEventId`: `string` \| `null`; `targetModuleId`: `string` \| `null`; `type`: `"RELATIONAL"` \| `"TEMPORAL"`; `updatedAt`: `Date`; \}\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:72](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/gantt/db-constraints.ts#L72)

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
