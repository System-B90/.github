[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/base](../index.md) / ClientGantApiBuilderProps

# Type Alias: ClientGantApiBuilderProps\<TEntity, _TCreatePayload\>

> **ClientGantApiBuilderProps**\<`TEntity`, `_TCreatePayload`\> = `object`

Defined in: [ui/src/api-client/gantt/base.ts:48](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/base.ts#L48)

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

### _TCreatePayload

`_TCreatePayload` = `Omit`\<`TEntity`, `"id"`\>

## Properties

### apiBaseUrl

> **apiBaseUrl**: `string`

Defined in: [ui/src/api-client/gantt/base.ts:52](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/base.ts#L52)

***

### dateFixup

> **dateFixup**: [`DateFixup`](DateFixup.md)\<`TEntity` & [`RawBaseDocument`](../../../../api-shared/types/gantt/api-layer/type-aliases/RawBaseDocument.md)\>

Defined in: [ui/src/api-client/gantt/base.ts:53](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/base.ts#L53)
