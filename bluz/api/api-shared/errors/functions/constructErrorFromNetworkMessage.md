[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/errors](../index.md) / constructErrorFromNetworkMessage

# Function: constructErrorFromNetworkMessage()

> **constructErrorFromNetworkMessage**(`networkMessage`): `ClientApiError`

Defined in: [ui/src/api-shared/errors.ts:67](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/errors.ts#L67)

Builds a `ClientApiError` (or the matching named subclass) from a server
error payload, so `instanceof` checks against subclasses like
`UserNotLoggedInError` work on the reconstructed client-side error.

## Parameters

### networkMessage

`ClientApiError`

## Returns

`ClientApiError`
