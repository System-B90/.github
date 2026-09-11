[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/cli-handoff](../index.md) / CLI\_HANDOFF\_TTL\_SECONDS

# Variable: CLI\_HANDOFF\_TTL\_SECONDS

> `const` **CLI\_HANDOFF\_TTL\_SECONDS**: `120` = `120`

Defined in: [ui/src/api-shared/types/cli-handoff.ts:35](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/cli-handoff.ts#L35)

How long a handoff code is redeemable for. Kept short: the whole login
round trip (page load, loopback fetch/navigation, CLI's HTTPS redeem call)
normally completes in a few seconds.
