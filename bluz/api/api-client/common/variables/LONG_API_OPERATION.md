[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/common](../index.md) / LONG\_API\_OPERATION

# Variable: LONG\_API\_OPERATION

> `const` **LONG\_API\_OPERATION**: `object`

Defined in: [ui/src/api-client/common.ts:22](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-client/common.ts#L22)

Ceiling for bulk server-side operations (cut, reload, restore, sync). They
routinely outlive the default, and aborting the fetch does not stop the
server: the user saw "aborted", retried, and ran the write twice.

## Type Declaration

### timeoutMs

> `readonly` **timeoutMs**: `number`
