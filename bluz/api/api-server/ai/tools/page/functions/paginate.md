[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/page](../index.md) / paginate

# Function: paginate()

> **paginate**\<`T`\>(`items`, `args`): [`Page`](../type-aliases/Page.md)\<`T`\>

Defined in: [ui/src/api-server/ai/tools/page.ts:44](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/ai/tools/page.ts#L44)

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
