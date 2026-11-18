[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/errors](../index.md) / GoogleReauthRequiredError

# Class: GoogleReauthRequiredError

Defined in: [ui/src/api-shared/errors.ts:33](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-shared/errors.ts#L33)

The user's stored Google refresh token was expired or revoked
(`invalid_grant`): the link exists but cannot act until the user reconnects
(#914). Served as 401 so it never reads as a server fault.

## Extends

- `ClientApiError`

## Constructors

### Constructor

> **new GoogleReauthRequiredError**(`message?`): `GoogleReauthRequiredError`

Defined in: [ui/src/api-shared/errors.ts:35](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-shared/errors.ts#L35)

#### Parameters

##### message?

`string` = `"חיבור Google Calendar פג תוקף — יש להתחבר מחדש"`

#### Returns

`GoogleReauthRequiredError`

#### Overrides

`ClientApiError.constructor`
