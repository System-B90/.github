[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/ai](../index.md) / isAiConfigured

# Function: isAiConfigured()

> **isAiConfigured**(`apiKeyOverride?`): `boolean`

Defined in: [ui/src/api-server/ai/index.ts:112](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/ai/index.ts#L112)

Whether the deployment can serve AI requests at all.

## Parameters

### apiKeyOverride?

`string`

A user's own key, which alone can satisfy this even
when the server has no key of its own configured.

## Returns

`boolean`
