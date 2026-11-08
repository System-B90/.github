[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/base](../index.md) / BasicGantApi

# Type Alias: BasicGantApi\<TEntity, TCreatePayload\>

> **BasicGantApi**\<`TEntity`, `TCreatePayload`\> = `object`

Defined in: [ui/src/api-client/gantt/base.ts:68](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-client/gantt/base.ts#L68)

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

### TCreatePayload

`TCreatePayload` = `Omit`\<`TEntity`, `"id"`\>

## Properties

### apiCreate

> `readonly` **apiCreate**: (`payload`, `options?`) => `Promise`\<`TEntity` & [`BaseDocument`](BaseDocument.md)\>

Defined in: [ui/src/api-client/gantt/base.ts:86](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-client/gantt/base.ts#L86)

#### Parameters

##### payload

`TCreatePayload`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`TEntity` & [`BaseDocument`](BaseDocument.md)\>

***

### apiDelete

> `readonly` **apiDelete**: (`id`, `options?`) => `Promise`\<`void`\>

Defined in: [ui/src/api-client/gantt/base.ts:94](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-client/gantt/base.ts#L94)

#### Parameters

##### id

`TEntity`\[`"id"`\]

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`void`\>

***

### apiGet

> `readonly` **apiGet**: (`id`, `options?`) => `Promise`\<[`ApiT`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiT.md)\<`TEntity` & [`BaseDocument`](BaseDocument.md)\>\>

Defined in: [ui/src/api-client/gantt/base.ts:82](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-client/gantt/base.ts#L82)

#### Parameters

##### id

`TEntity`\[`"id"`\]

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<[`ApiT`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiT.md)\<`TEntity` & [`BaseDocument`](BaseDocument.md)\>\>

***

### apiGetMany

> `readonly` **apiGetMany**: (`ids`, `options?`) => `Promise`\<`Record`\<`TEntity`\[`"id"`\], `TEntity` & [`BaseDocument`](BaseDocument.md)\>\>

Defined in: [ui/src/api-client/gantt/base.ts:98](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-client/gantt/base.ts#L98)

#### Parameters

##### ids

`TEntity`\[`"id"`\][]

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`Record`\<`TEntity`\[`"id"`\], `TEntity` & [`BaseDocument`](BaseDocument.md)\>\>

***

### apiLink

> `readonly` **apiLink**: (`itemId`, `newParentId`, `options?`) => `Promise`\<`TEntity` & [`BaseDocument`](BaseDocument.md)\>

Defined in: [ui/src/api-client/gantt/base.ts:102](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-client/gantt/base.ts#L102)

#### Parameters

##### itemId

`TEntity`\[`"id"`\]

##### newParentId

[`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)\[`"id"`\]

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`TEntity` & [`BaseDocument`](BaseDocument.md)\>

***

### apiList

> `readonly` **apiList**: (`options?`) => `Promise`\<`Record`\<`TEntity`\[`"id"`\], `TEntity`\[`"title"`\]\>\>

Defined in: [ui/src/api-client/gantt/base.ts:72](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-client/gantt/base.ts#L72)

#### Parameters

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`Record`\<`TEntity`\[`"id"`\], `TEntity`\[`"title"`\]\>\>

***

### apiListWithParents

> `readonly` **apiListWithParents**: (`options?`) => `Promise`\<`Record`\<`TEntity`\[`"id"`\], [`ListEntryWithParent`](ListEntryWithParent.md)\<`TEntity`\>\>\>

Defined in: [ui/src/api-client/gantt/base.ts:79](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-client/gantt/base.ts#L79)

Same listing as `apiList`, but each value carries the parent id. Use
when you need child → parent without fetching each item. See #310.

#### Parameters

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`Record`\<`TEntity`\[`"id"`\], [`ListEntryWithParent`](ListEntryWithParent.md)\<`TEntity`\>\>\>

***

### apiUnlink

> `readonly` **apiUnlink**: (`itemId`, `oldParentId`, `options?`) => `Promise`\<`void`\>

Defined in: [ui/src/api-client/gantt/base.ts:107](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-client/gantt/base.ts#L107)

#### Parameters

##### itemId

`TEntity`\[`"id"`\]

##### oldParentId

[`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)\[`"id"`\]

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`void`\>

***

### apiUpdate

> `readonly` **apiUpdate**: (`updates`, `options?`) => `Promise`\<`TEntity` & [`BaseDocument`](BaseDocument.md)\>

Defined in: [ui/src/api-client/gantt/base.ts:90](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-client/gantt/base.ts#L90)

#### Parameters

##### updates

`Partial`\<`TEntity`\> & `object`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`TEntity` & [`BaseDocument`](BaseDocument.md)\>
