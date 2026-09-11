[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / pushEventToGoogle

# Function: pushEventToGoogle()

> **pushEventToGoogle**(`userId`, `event`, `action`, `iterationId?`): `Promise`\<`boolean`\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:240](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/google/google-calendar-service.ts#L240)

Push a single Bluz event to the user's Bluz Google calendar. Silent no-op
when the integration isn't configured/connected, or when Google is
unreachable (offline-hosted deployments must never fail on this).

## Parameters

### userId

`string`

### event

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

### action

`"delete"` \| `"upsert"`

### iterationId?

`string`

## Returns

`Promise`\<`boolean`\>
