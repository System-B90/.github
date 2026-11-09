[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / STUDENT\_CLIENT\_TIME\_HEADER

# Variable: STUDENT\_CLIENT\_TIME\_HEADER

> `const` **STUDENT\_CLIENT\_TIME\_HEADER**: `"x-bluz-client-time"` = `"x-bluz-client-time"`

Defined in: [ui/src/api-shared/types/student-view.ts:179](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/student-view.ts#L179)

Sent with every `/api/server-time` request: the device clock, epoch ms. Only
ever compared against the server clock — nothing is computed from it.
