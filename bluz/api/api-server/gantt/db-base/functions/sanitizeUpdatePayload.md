[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-base](../index.md) / sanitizeUpdatePayload

# Function: sanitizeUpdatePayload()

> **sanitizeUpdatePayload**(`table`, `data`, `typeName`): `Record`\<`string`, `unknown`\>

Defined in: [ui/src/api-server/gantt/db-base.ts:122](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/gantt/db-base.ts#L122)

The update-path counterpart of [sanitizeCreatePayload](sanitizeCreatePayload.md): same column
allow-list and same enum validation, minus the required-field check (a PATCH
is partial by definition).

Without it `updateItem` spread the raw client body straight into `.set()`,
so every column except the server-owned three was client-writable and a
typo'd field became an opaque 500 instead of a dropped no-op (#519).

## Parameters

### table

`PgTableWithColumns`\<`any`\>

### data

`Record`\<`string`, `unknown`\>

### typeName

`string`

## Returns

`Record`\<`string`, `unknown`\>
