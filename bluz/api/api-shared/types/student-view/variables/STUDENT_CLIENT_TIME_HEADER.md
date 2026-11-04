[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / STUDENT\_CLIENT\_TIME\_HEADER

# Variable: STUDENT\_CLIENT\_TIME\_HEADER

> `const` **STUDENT\_CLIENT\_TIME\_HEADER**: `"x-bluz-client-time"` = `"x-bluz-client-time"`

Defined in: [ui/src/api-shared/types/student-view.ts:160](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/types/student-view.ts#L160)

Sent with every `/api/server-time` request: the device clock, epoch ms. Only
ever compared against the server clock — nothing is computed from it.
