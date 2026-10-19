[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/event/route](../index.md) / PATCH

# Variable: PATCH

> `const` **PATCH**: [`ServerApi`](../../../../../api-server/common/type-aliases/ServerApi.md)\<[`ApiEventUpdateManyPayload`](../../../../../api-shared/types/event/type-aliases/ApiEventUpdateManyPayload.md), [`ApiEventUpdateManyResponse`](../../../../../api-shared/types/event/type-aliases/ApiEventUpdateManyResponse.md)\>

Defined in: [ui/src/app/api/event/route.ts:156](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/app/api/event/route.ts#L156)

Bulk update (#932): the body is an array of events. One bulkWrite and one
history insert instead of a request per event.
