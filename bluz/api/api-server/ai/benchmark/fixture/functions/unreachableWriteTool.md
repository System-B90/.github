[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/fixture](../index.md) / unreachableWriteTool

# Function: unreachableWriteTool()

> **unreachableWriteTool**(`name`, `title`, `description`, `danger`, `parameters`): [`AiTool`](../../../tools/types/type-aliases/AiTool.md)\<`Record`\<`string`, `unknown`\>\>

Defined in: [ui/src/api-server/ai/benchmark/fixture.ts:384](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/ai/benchmark/fixture.ts#L384)

Builds a write tool that cannot write.

It exists so the model is *offered* a destructive option and its restraint
can be measured. The benchmark never approves a call, so `execute` is
unreachable through the gate — and throws if that ever stops being true,
rather than quietly pretending to have succeeded.

## Parameters

### name

`string`

### title

`string`

### description

`string`

### danger

[`AiToolDanger`](../../../../../api-shared/types/ai/enumerations/AiToolDanger.md)

### parameters

`Record`\<`string`, `unknown`\>

## Returns

[`AiTool`](../../../tools/types/type-aliases/AiTool.md)\<`Record`\<`string`, `unknown`\>\>
