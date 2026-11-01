[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/errors](../index.md) / GoogleReauthRequiredError

# Class: GoogleReauthRequiredError

Defined in: [ui/src/api-shared/errors.ts:33](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/errors.ts#L33)

The user's stored Google refresh token was expired or revoked
(`invalid_grant`): the link exists but cannot act until the user reconnects
(#914). Served as 401 so it never reads as a server fault.

## Extends

- `ClientApiError`

## Constructors

### Constructor

> **new GoogleReauthRequiredError**(`message?`): `GoogleReauthRequiredError`

Defined in: [ui/src/api-shared/errors.ts:35](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/errors.ts#L35)

#### Parameters

##### message?

`string` = `"חיבור Google Calendar פג תוקף — יש להתחבר מחדש"`

#### Returns

`GoogleReauthRequiredError`

#### Overrides

`ClientApiError.constructor`
