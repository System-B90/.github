[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/ai](../index.md) / isAiConfigured

# Function: isAiConfigured()

> **isAiConfigured**(`apiKeyOverride?`): `boolean`

Defined in: [ui/src/api-server/ai/index.ts:112](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/index.ts#L112)

Whether the deployment can serve AI requests at all.

## Parameters

### apiKeyOverride?

`string`

A user's own key, which alone can satisfy this even
when the server has no key of its own configured.

## Returns

`boolean`
