[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/ai](../index.md) / isAiConfigured

# Function: isAiConfigured()

> **isAiConfigured**(`apiKeyOverride?`): `boolean`

Defined in: [ui/src/api-server/ai/index.ts:101](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/ai/index.ts#L101)

Whether the deployment can serve AI requests at all.

## Parameters

### apiKeyOverride?

`string`

A user's own key, which alone can satisfy this even
when the server has no key of its own configured.

## Returns

`boolean`
