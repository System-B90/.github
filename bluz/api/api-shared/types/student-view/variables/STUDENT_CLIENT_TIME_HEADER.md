[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / STUDENT\_CLIENT\_TIME\_HEADER

# Variable: STUDENT\_CLIENT\_TIME\_HEADER

> `const` **STUDENT\_CLIENT\_TIME\_HEADER**: `"x-bluz-client-time"` = `"x-bluz-client-time"`

Defined in: [ui/src/api-shared/types/student-view.ts:185](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L185)

Sent with every `/api/server-time` request: the device clock, epoch ms. Only
ever compared against the server clock — nothing is computed from it.
