[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/errors](../index.md) / HiveSessionRequiredError

# Class: HiveSessionRequiredError

Defined in: [ui/src/api-shared/errors.ts:93](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/errors.ts#L93)

Hive was asked for on behalf of a personal access token. Tokens carry no
Hive credentials of their own, and borrowing the service account would hand
the caller that account's (broader) Hive view, so these calls are refused.
Served as 403 with this message, unlike a generic ForbiddenError.

## Extends

- `ClientApiError`

## Constructors

### Constructor

> **new HiveSessionRequiredError**(`message?`): `HiveSessionRequiredError`

Defined in: [ui/src/api-shared/errors.ts:95](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/errors.ts#L95)

#### Parameters

##### message?

`string` = `"נתוני Hive זמינים רק בהתחברות אישית (דפדפן או bluz login), לא דרך טוקן גישה."`

#### Returns

`HiveSessionRequiredError`

#### Overrides

`ClientApiError.constructor`
