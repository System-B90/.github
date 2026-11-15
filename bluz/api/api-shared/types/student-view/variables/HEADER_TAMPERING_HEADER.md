[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / HEADER\_TAMPERING\_HEADER

# Variable: HEADER\_TAMPERING\_HEADER

> `const` **HEADER\_TAMPERING\_HEADER**: `"x-bluz-header-tampering"` = `"x-bluz-header-tampering"`

Defined in: [ui/src/api-shared/types/student-view.ts:209](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-shared/types/student-view.ts#L209)

Set by nginx only (`nginx/bluz/header-tampering.conf`): the names of the
suspicious headers it stripped from this request. nginx omits it when there
were none, and overwrites any value a client sends.
