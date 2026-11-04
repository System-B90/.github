[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/base](../index.md) / ClientGantApiBuilderProps

# Type Alias: ClientGantApiBuilderProps\<TEntity, _TCreatePayload\>

> **ClientGantApiBuilderProps**\<`TEntity`, `_TCreatePayload`\> = `object`

Defined in: [ui/src/api-client/gantt/base.ts:50](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-client/gantt/base.ts#L50)

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

### _TCreatePayload

`_TCreatePayload` = `Omit`\<`TEntity`, `"id"`\>

## Properties

### apiBaseUrl

> **apiBaseUrl**: `string`

Defined in: [ui/src/api-client/gantt/base.ts:54](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-client/gantt/base.ts#L54)

***

### dateFixup

> **dateFixup**: [`DateFixup`](DateFixup.md)\<`TEntity` & [`RawBaseDocument`](../../../../api-shared/types/gantt/api-layer/type-aliases/RawBaseDocument.md)\>

Defined in: [ui/src/api-client/gantt/base.ts:55](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-client/gantt/base.ts#L55)
