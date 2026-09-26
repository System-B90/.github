[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / pushEventToGoogle

# Function: pushEventToGoogle()

> **pushEventToGoogle**(`userId`, `event`, `action`, `iterationId?`): `Promise`\<`boolean`\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:613](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/google/google-calendar-service.ts#L613)

Push a single Bluz event to the user's linked Google calendar. Silent no-op
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
