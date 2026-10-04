[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/ai](../index.md) / getAiProvider

# Function: getAiProvider()

> **getAiProvider**(`apiKeyOverride?`): [`AiProvider`](../provider/type-aliases/AiProvider.md)

Defined in: [ui/src/api-server/ai/index.ts:80](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/ai/index.ts#L80)

## Parameters

### apiKeyOverride?

`string`

A user's own key (personal settings), used instead of
the server's own key when present — for whichever provider `AI_PROVIDER`
currently names.

## Returns

[`AiProvider`](../provider/type-aliases/AiProvider.md)

The configured provider.

## Throws

AiNotConfiguredError when `AI_PROVIDER` names something unknown, or
the selected provider has no credentials.
