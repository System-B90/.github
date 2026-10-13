[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/common](../index.md) / ServerApiWithParams

# Type Alias: ServerApiWithParams\<PayloadT, ResponseT, ParamsT\>

> **ServerApiWithParams**\<`PayloadT`, `ResponseT`, `ParamsT`\> = (`request`, `context`) => `Promise`\<`NextResponse`\<`ResponseT`\> \| `Response`\>

Defined in: [ui/src/api-server/common.ts:324](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/common.ts#L324)

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
