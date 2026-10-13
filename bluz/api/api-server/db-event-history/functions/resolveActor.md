[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/db-event-history](../index.md) / resolveActor

# Function: resolveActor()

> **resolveActor**(): `Promise`\<\{ `displayName`: `string`; `id`: `string`; \} \| `null`\>

Defined in: [ui/src/api-server/db-event-history.ts:48](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/db-event-history.ts#L48)

Resolve the acting user once, for reuse across a bulk write.

## Returns

`Promise`\<\{ `displayName`: `string`; `id`: `string`; \} \| `null`\>

The session user, or null outside a request scope / for machines.
