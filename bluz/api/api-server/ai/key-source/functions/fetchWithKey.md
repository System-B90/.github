[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/key-source](../index.md) / fetchWithKey

# Function: fetchWithKey()

> **fetchWithKey**(`key`, `authHeaders`, `url`, `init`): `Promise`\<`Response`\>

Defined in: [ui/src/api-server/ai/key-source.ts:30](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/key-source.ts#L30)

`aiFetch` with auth headers built from the current token, retried once on
a 401 from an expiring key.

## Parameters

### key

[`AiKeySource`](../type-aliases/AiKeySource.md)

### authHeaders

(`token`) => `Record`\<`string`, `string`\>

The wire format's auth headers for a token.

### url

`string`

### init

`RequestInit`

## Returns

`Promise`\<`Response`\>
