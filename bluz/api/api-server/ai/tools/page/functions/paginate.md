[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/page](../index.md) / paginate

# Function: paginate()

> **paginate**\<`T`\>(`items`, `args`): [`Page`](../type-aliases/Page.md)\<`T`\>

Defined in: [ui/src/api-server/ai/tools/page.ts:40](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/ai/tools/page.ts#L40)

Slices a list to one page, and says so: a model shown 50 of 400 rooms must
know there are 400, or it reports the wrong count with confidence.

## Type Parameters

### T

`T`

## Parameters

### items

`T`[]

### args

[`PageArgs`](../type-aliases/PageArgs.md)

## Returns

[`Page`](../type-aliases/Page.md)\<`T`\>
