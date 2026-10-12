[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/errors](../index.md) / GoogleReauthRequiredError

# Class: GoogleReauthRequiredError

Defined in: [ui/src/api-shared/errors.ts:33](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-shared/errors.ts#L33)

The user's stored Google refresh token was expired or revoked
(`invalid_grant`): the link exists but cannot act until the user reconnects
(#914). Served as 401 so it never reads as a server fault.

## Extends

- `ClientApiError`

## Constructors

### Constructor

> **new GoogleReauthRequiredError**(`message?`): `GoogleReauthRequiredError`

Defined in: [ui/src/api-shared/errors.ts:34](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-shared/errors.ts#L34)

#### Parameters

##### message?

`string` = `"חיבור Google Calendar פג תוקף — יש להתחבר מחדש"`

#### Returns

`GoogleReauthRequiredError`

#### Overrides

`ClientApiError.constructor`
