[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/base](../index.md) / ClientGantApiBuilderProps

# Type Alias: ClientGantApiBuilderProps\<TEntity, _TCreatePayload\>

> **ClientGantApiBuilderProps**\<`TEntity`, `_TCreatePayload`\> = `object`

Defined in: [ui/src/api-client/gantt/base.ts:48](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-client/gantt/base.ts#L48)

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

### _TCreatePayload

`_TCreatePayload` = `Omit`\<`TEntity`, `"id"`\>

## Properties

### apiBaseUrl

> **apiBaseUrl**: `string`

Defined in: [ui/src/api-client/gantt/base.ts:52](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-client/gantt/base.ts#L52)

***

### dateFixup

> **dateFixup**: [`DateFixup`](DateFixup.md)\<`TEntity` & [`RawBaseDocument`](../../../../api-shared/types/gantt/api-layer/type-aliases/RawBaseDocument.md)\>

Defined in: [ui/src/api-client/gantt/base.ts:53](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-client/gantt/base.ts#L53)
