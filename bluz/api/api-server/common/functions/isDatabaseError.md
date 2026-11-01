[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/common](../index.md) / isDatabaseError

# Function: isDatabaseError()

> **isDatabaseError**(`e`): `boolean`

Defined in: [ui/src/api-server/common.ts:233](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/common.ts#L233)

Detects a raw database driver error (postgres.js `PostgresError`, identified
by its `name` or a 5-char SQLSTATE `code`). These carry internal details —
table/column/constraint names, the offending SQL — that must never reach the
client (#162), so they are collapsed into an opaque 500 by [catchHandler](catchHandler.md)
rather than surfaced verbatim.

## Parameters

### e

`unknown`

## Returns

`boolean`
