[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/common](../index.md) / ServerApiWithParams

# Type Alias: ServerApiWithParams\<PayloadT, ResponseT, ParamsT\>

> **ServerApiWithParams**\<`PayloadT`, `ResponseT`, `ParamsT`\> = (`request`, `context`) => `Promise`\<`NextResponse`\<`ResponseT`\> \| `Response`\>

Defined in: [ui/src/api-server/common.ts:313](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/common.ts#L313)

## Type Parameters

### PayloadT

`PayloadT`

### ResponseT

`ResponseT`

### ParamsT

`ParamsT`

## Parameters

### request

[`ServerApiRequest`](ServerApiRequest.md)\<`PayloadT`\>

### context

#### params

`Promise`\<`ParamsT`\>

## Returns

`Promise`\<`NextResponse`\<`ResponseT`\> \| `Response`\>
