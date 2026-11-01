[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-security-log](../index.md) / currentRequestIp

# Function: currentRequestIp()

> **currentRequestIp**(): `Promise`\<`string` \| `undefined`\>

Defined in: [ui/src/api-server/student-security-log.ts:52](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/student-security-log.ts#L52)

The caller's address, as nginx saw it; undefined outside a request.

`X-Real-IP` first: nginx *sets* it to `$remote_addr`, overwriting anything
the client sent. `X-Forwarded-For` is only a fallback, and read from the
end — nginx appends the real address, while every entry before it is
whatever the client claimed, so the first one is trivially spoofed.

## Returns

`Promise`\<`string` \| `undefined`\>
