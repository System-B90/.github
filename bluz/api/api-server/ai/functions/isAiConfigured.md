[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/ai](../index.md) / isAiConfigured

# Function: isAiConfigured()

> **isAiConfigured**(`apiKeyOverride?`): `boolean`

Defined in: [ui/src/api-server/ai/index.ts:101](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/ai/index.ts#L101)

Whether the deployment can serve AI requests at all.

## Parameters

### apiKeyOverride?

`string`

A user's own key, which alone can satisfy this even
when the server has no key of its own configured.

## Returns

`boolean`
