[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/common](../index.md) / ServerApiWithParams

# Type Alias: ServerApiWithParams\<PayloadT, ResponseT, ParamsT\>

> **ServerApiWithParams**\<`PayloadT`, `ResponseT`, `ParamsT`\> = (`request`, `context`) => `Promise`\<`NextResponse`\<`ResponseT`\> \| `Response`\>

Defined in: [ui/src/api-server/common.ts:394](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/common.ts#L394)

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
