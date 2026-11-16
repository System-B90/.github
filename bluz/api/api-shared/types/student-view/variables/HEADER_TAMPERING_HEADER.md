[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / HEADER\_TAMPERING\_HEADER

# Variable: HEADER\_TAMPERING\_HEADER

> `const` **HEADER\_TAMPERING\_HEADER**: `"x-bluz-header-tampering"` = `"x-bluz-header-tampering"`

Defined in: [ui/src/api-shared/types/student-view.ts:209](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/api-shared/types/student-view.ts#L209)

Set by nginx only (`nginx/bluz/header-tampering.conf`): the names of the
suspicious headers it stripped from this request. nginx omits it when there
were none, and overwrites any value a client sends.
