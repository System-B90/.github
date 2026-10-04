[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/cli-handoff](../index.md) / CLI\_HANDOFF\_TTL\_SECONDS

# Variable: CLI\_HANDOFF\_TTL\_SECONDS

> `const` **CLI\_HANDOFF\_TTL\_SECONDS**: `120` = `120`

Defined in: [ui/src/api-shared/types/cli-handoff.ts:35](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/cli-handoff.ts#L35)

How long a handoff code is redeemable for. Kept short: the whole login
round trip (page load, loopback fetch/navigation, CLI's HTTPS redeem call)
normally completes in a few seconds.
