[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/cli-handoff](../index.md) / CliHandoffCode

# Type Alias: CliHandoffCode

> **CliHandoffCode** = `object`

Defined in: [ui/src/api-shared/types/cli-handoff.ts:25](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/cli-handoff.ts#L25)

One outstanding CLI login handoff. `code` is the lookup key (opaque,
crypto.randomBytes-derived — never the verification code shown on screen,
which only guards the loopback callback, see #521). `sealedToken` is the
next-auth session token encrypted at rest with `secret-box.ts` — never
stored in the clear.

Redemption (`POST /api/cli-auth/redeem`) is a `findOneAndDelete` by `code`,
which is what makes the code single-use: the delete *is* the "already
redeemed" guard, the same insert/delete-as-claim pattern as
`CurriculumCutClaim` and `HiveLessonActivation`. `createdAt` backs a Mongo
TTL index as a backstop for codes nobody redeems; redemption also checks
the age itself so expiry is enforced immediately rather than only at the
next TTL sweep (which runs on a ~60s cadence).

## Properties

### code

> **code**: `string`

Defined in: [ui/src/api-shared/types/cli-handoff.ts:26](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/cli-handoff.ts#L26)

***

### createdAt

> **createdAt**: `Date`

Defined in: [ui/src/api-shared/types/cli-handoff.ts:29](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/cli-handoff.ts#L29)

***

### sealedToken

> **sealedToken**: `string`

Defined in: [ui/src/api-shared/types/cli-handoff.ts:27](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/cli-handoff.ts#L27)

***

### userId

> **userId**: `string`

Defined in: [ui/src/api-shared/types/cli-handoff.ts:28](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/cli-handoff.ts#L28)
