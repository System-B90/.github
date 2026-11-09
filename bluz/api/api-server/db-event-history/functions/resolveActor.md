[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/db-event-history](../index.md) / resolveActor

# Function: resolveActor()

> **resolveActor**(): `Promise`\<\{ `displayName`: `string`; `id`: `string`; \} \| `null`\>

Defined in: [ui/src/api-server/db-event-history.ts:48](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/db-event-history.ts#L48)

Resolve the acting user once, for reuse across a bulk write.

## Returns

`Promise`\<\{ `displayName`: `string`; `id`: `string`; \} \| `null`\>

The session user, or null outside a request scope / for machines.
