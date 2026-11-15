[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / STUDENT\_CLIENT\_TIME\_HEADER

# Variable: STUDENT\_CLIENT\_TIME\_HEADER

> `const` **STUDENT\_CLIENT\_TIME\_HEADER**: `"x-bluz-client-time"` = `"x-bluz-client-time"`

Defined in: [ui/src/api-shared/types/student-view.ts:185](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/api-shared/types/student-view.ts#L185)

Sent with every `/api/server-time` request: the device clock, epoch ms. Only
ever compared against the server clock — nothing is computed from it.
