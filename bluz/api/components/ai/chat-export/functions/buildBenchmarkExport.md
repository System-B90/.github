[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/ai/chat-export](../index.md) / buildBenchmarkExport

# Function: buildBenchmarkExport()

> **buildBenchmarkExport**(`result`, `exportedAt`): `object`

Defined in: [ui/src/components/ai/chat-export.ts:133](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/ai/chat-export.ts#L133)

JSON export of a self-test run: the system prompt once, then per case the
prompt, verdicts, and the full transcript (tool calls with raw arguments and
results) — what is needed to see why a tool or prompt misfired.

## Parameters

### result

[`AiBenchmarkResult`](../../../../api-shared/types/ai-benchmark/type-aliases/AiBenchmarkResult.md)

### exportedAt

`Date`

## Returns

`object`

### content

> **content**: `string`

### fileName

> **fileName**: `string`

### mimeType

> **mimeType**: `string`
