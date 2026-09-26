[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/common](../index.md) / isDatabaseError

# Function: isDatabaseError()

> **isDatabaseError**(`e`): `boolean`

Defined in: [ui/src/api-server/common.ts:199](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/common.ts#L199)

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
