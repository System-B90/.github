[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / getRequestAuth

# Function: getRequestAuth()

> **getRequestAuth**(): `Promise`\<[`RequestAuth`](../type-aliases/RequestAuth.md) \| `null`\>

Defined in: [ui/src/api-server/session-user.ts:79](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/session-user.ts#L79)

Resolve the caller: the next-auth session cookie first, else a personal
access token. A cookie wins when both are sent — the browser never sends a
token, and the CLI never sends both.

## Returns

`Promise`\<[`RequestAuth`](../type-aliases/RequestAuth.md) \| `null`\>

## Throws

ForbiddenError when a ReadOnly token is used for anything but GET/HEAD.
