[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/errors](../index.md) / constructErrorFromNetworkMessage

# Function: constructErrorFromNetworkMessage()

> **constructErrorFromNetworkMessage**(`networkMessage`): `ClientApiError`

Defined in: [ui/src/api-shared/errors.ts:67](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/errors.ts#L67)

Builds a `ClientApiError` (or the matching named subclass) from a server
error payload, so `instanceof` checks against subclasses like
`UserNotLoggedInError` work on the reconstructed client-side error.

## Parameters

### networkMessage

`ClientApiError`

## Returns

`ClientApiError`
