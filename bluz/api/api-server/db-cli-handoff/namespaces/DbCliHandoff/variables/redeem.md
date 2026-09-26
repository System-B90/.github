[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-cli-handoff](../../../index.md) / [DbCliHandoff](../index.md) / redeem

# Variable: redeem

> `const` **redeem**: (`code`) => `Promise`\<`string`\> = `redeemHandoffCode`

Defined in: [ui/src/api-server/db-cli-handoff.ts:78](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/db-cli-handoff.ts#L78)

Redeem a handoff code for its session token exactly once.

`findOneAndDelete` makes the delete *and* the lookup a single atomic step:
a second, concurrent redemption of the same code loses the race and finds
nothing, so "already redeemed" and "unknown code" are indistinguishable by
design (no oracle for guessing). Expiry is checked against `createdAt`
directly rather than relying solely on the Mongo TTL index, which only
sweeps on a ~60s cadence — without this a code could be redeemed well past
its nominal TTL.

## Parameters

### code

`string`

## Returns

`Promise`\<`string`\>

## Throws

ClientApiError when the code is unknown, already used, or expired.
