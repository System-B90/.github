[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/common](../index.md) / LONG\_API\_OPERATION

# Variable: LONG\_API\_OPERATION

> `const` **LONG\_API\_OPERATION**: `object`

Defined in: [ui/src/api-client/common.ts:22](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-client/common.ts#L22)

Ceiling for bulk server-side operations (cut, reload, restore, sync). They
routinely outlive the default, and aborting the fetch does not stop the
server: the user saw "aborted", retried, and ran the write twice.

## Type Declaration

### timeoutMs

> `readonly` **timeoutMs**: `number`
