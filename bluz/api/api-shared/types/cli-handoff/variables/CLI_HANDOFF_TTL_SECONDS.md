[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/cli-handoff](../index.md) / CLI\_HANDOFF\_TTL\_SECONDS

# Variable: CLI\_HANDOFF\_TTL\_SECONDS

> `const` **CLI\_HANDOFF\_TTL\_SECONDS**: `120` = `120`

Defined in: [ui/src/api-shared/types/cli-handoff.ts:35](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/cli-handoff.ts#L35)

How long a handoff code is redeemable for. Kept short: the whole login
round trip (page load, loopback fetch/navigation, CLI's HTTPS redeem call)
normally completes in a few seconds.
