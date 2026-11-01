[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-base](../index.md) / postgresErrorCode

# Function: postgresErrorCode()

> **postgresErrorCode**(`error`): `string` \| `undefined`

Defined in: [ui/src/api-server/gantt/db-base.ts:26](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/gantt/db-base.ts#L26)

The SQLSTATE of a failed query, wherever the driver put it.

postgres.js sets `code` on the error itself; Drizzle wraps that error and
exposes the original under `cause`. Reading only one of the two silently
misses every constraint violation raised through the other path, so the
caller falls through to its generic "something failed" message.

## Parameters

### error

`unknown`

## Returns

`string` \| `undefined`
