[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/key-source](../index.md) / AiKeySource

# Type Alias: AiKeySource

> **AiKeySource** = `object`

Defined in: [ui/src/api-server/ai/key-source.ts:14](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/key-source.ts#L14)

Where the token comes from. A plain key never changes; a helper-issued one
(an SSO token) expires, so it is fetched per request and, when `invalidate`
exists, a 401 drops it and the request is retried once.

## Properties

### get

> **get**: (`signal?`) => `Promise`\<`string`\>

Defined in: [ui/src/api-server/ai/key-source.ts:16](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/key-source.ts#L16)

#### Parameters

##### signal?

`AbortSignal`

The caller gave up; a slow source stops waiting.

#### Returns

`Promise`\<`string`\>

***

### invalidate?

> `optional` **invalidate?**: () => `void`

Defined in: [ui/src/api-server/ai/key-source.ts:17](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/key-source.ts#L17)

#### Returns

`void`
