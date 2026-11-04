[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / pushEventToGoogle

# Function: pushEventToGoogle()

> **pushEventToGoogle**(`userId`, `event`, `action`, `iterationId?`): `Promise`\<`boolean`\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:748](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/google/google-calendar-service.ts#L748)

Push a single Bluz event to the user's linked Google calendar. Silent no-op
when the integration isn't configured/connected, or when Google is
unreachable (offline-hosted deployments must never fail on this).

## Parameters

### userId

`string`

### event

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

### action

`"upsert"` \| `"delete"`

### iterationId?

`string`

## Returns

`Promise`\<`boolean`\>
