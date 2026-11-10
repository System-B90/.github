[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / getRequestAuth

# Function: getRequestAuth()

> **getRequestAuth**(): `Promise`\<[`RequestAuth`](../type-aliases/RequestAuth.md) \| `null`\>

Defined in: [ui/src/api-server/session-user.ts:85](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/session-user.ts#L85)

Resolve the caller: the next-auth session cookie first, else a personal
access token. A cookie wins when both are sent — the browser never sends a
token, and the CLI never sends both.

## Returns

`Promise`\<[`RequestAuth`](../type-aliases/RequestAuth.md) \| `null`\>

## Throws

ForbiddenError when a ReadOnly token is used for anything but GET/HEAD.
