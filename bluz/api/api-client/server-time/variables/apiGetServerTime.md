[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/server-time](../index.md) / apiGetServerTime

# Variable: apiGetServerTime

> `const` **apiGetServerTime**: [`ClientApiNoPayload`](../../common/type-aliases/ClientApiNoPayload.md)\<[`ApiServerTimeGetResponse`](../../../api-shared/types/server-time/type-aliases/ApiServerTimeGetResponse.md)\>

Defined in: [ui/src/api-client/server-time.ts:13](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-client/server-time.ts#L13)

The server clock — the only source of "now" for the student board, and of
"today" for the staff calendar.

The device clock rides along as a header so the server can flag a student
who wound it. That is its only use: nothing on either side is computed
from it.
