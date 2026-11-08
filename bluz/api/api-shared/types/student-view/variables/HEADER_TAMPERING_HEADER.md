[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / HEADER\_TAMPERING\_HEADER

# Variable: HEADER\_TAMPERING\_HEADER

> `const` **HEADER\_TAMPERING\_HEADER**: `"x-bluz-header-tampering"` = `"x-bluz-header-tampering"`

Defined in: [ui/src/api-shared/types/student-view.ts:181](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types/student-view.ts#L181)

Set by nginx only (`nginx/bluz/header-tampering.conf`): the names of the
suspicious headers it stripped from this request. nginx omits it when there
were none, and overwrites any value a client sends.
