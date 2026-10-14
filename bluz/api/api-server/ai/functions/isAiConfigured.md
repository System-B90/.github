[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/ai](../index.md) / isAiConfigured

# Function: isAiConfigured()

> **isAiConfigured**(`apiKeyOverride?`): `boolean`

Defined in: [ui/src/api-server/ai/index.ts:101](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/ai/index.ts#L101)

Whether the deployment can serve AI requests at all.

## Parameters

### apiKeyOverride?

`string`

A user's own key, which alone can satisfy this even
when the server has no key of its own configured.

## Returns

`boolean`
