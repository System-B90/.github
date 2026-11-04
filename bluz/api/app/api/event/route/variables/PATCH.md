[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/event/route](../index.md) / PATCH

# Variable: PATCH

> `const` **PATCH**: [`ServerApi`](../../../../../api-server/common/type-aliases/ServerApi.md)\<[`ApiEventUpdateManyPayload`](../../../../../api-shared/types/event/type-aliases/ApiEventUpdateManyPayload.md), [`ApiEventUpdateManyResponse`](../../../../../api-shared/types/event/type-aliases/ApiEventUpdateManyResponse.md)\>

Defined in: [ui/src/app/api/event/route.ts:168](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/app/api/event/route.ts#L168)

Bulk update (#932): the body is an array of events. One bulkWrite and one
history insert instead of a request per event.
