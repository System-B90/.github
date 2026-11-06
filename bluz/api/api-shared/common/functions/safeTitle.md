[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/common](../index.md) / safeTitle

# Function: safeTitle()

> **safeTitle**(`title`): `string`

Defined in: [ui/src/api-shared/common.ts:29](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/common.ts#L29)

Sanitizes a human-readable title into a filesystem/URL-safe token.
Keeps ASCII alphanumerics and the Hebrew Unicode block (֐-׿); everything
else collapses to an underscore. Used for export filenames and the like.

## Parameters

### title

`string`

## Returns

`string`
