[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/db-event-history](../index.md) / resolveActor

# Function: resolveActor()

> **resolveActor**(): `Promise`\<\{ `displayName`: `string`; `id`: `string`; \} \| `null`\>

Defined in: [ui/src/api-server/db-event-history.ts:48](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/db-event-history.ts#L48)

Resolve the acting user once, for reuse across a bulk write.

## Returns

`Promise`\<\{ `displayName`: `string`; `id`: `string`; \} \| `null`\>

The session user, or null outside a request scope / for machines.
