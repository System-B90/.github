[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/errors](../index.md) / constructErrorFromNetworkMessage

# Function: constructErrorFromNetworkMessage()

> **constructErrorFromNetworkMessage**(`networkMessage`): `ClientApiError`

Defined in: [ui/src/api-shared/errors.ts:52](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-shared/errors.ts#L52)

Builds a `ClientApiError` (or the matching named subclass) from a server
error payload, so `instanceof` checks against subclasses like
`UserNotLoggedInError` work on the reconstructed client-side error.

## Parameters

### networkMessage

`ClientApiError`

## Returns

`ClientApiError`
