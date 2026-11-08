[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/common](../index.md) / ServerApiWithParams

# Type Alias: ServerApiWithParams\<PayloadT, ResponseT, ParamsT\>

> **ServerApiWithParams**\<`PayloadT`, `ResponseT`, `ParamsT`\> = (`request`, `context`) => `Promise`\<`NextResponse`\<`ResponseT`\> \| `Response`\>

Defined in: [ui/src/api-server/common.ts:394](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/common.ts#L394)

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
