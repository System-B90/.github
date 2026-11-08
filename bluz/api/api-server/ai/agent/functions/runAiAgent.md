[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/agent](../index.md) / runAiAgent

# Function: runAiAgent()

> **runAiAgent**(`options`): `AsyncGenerator`\<[`AiStreamEvent`](../../../../api-shared/types/ai/type-aliases/AiStreamEvent.md)\>

Defined in: [ui/src/api-server/ai/agent.ts:146](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/agent.ts#L146)

Runs one turn and yields it as a stream of app-level events.

The turn ends when the model stops calling tools, when a write needs
approval, when the model asks the human a question, or when
[AI\_MAX\_TOOL\_ITERATIONS](../../../../api-shared/types/ai/variables/AI_MAX_TOOL_ITERATIONS.md) is hit.

## Parameters

### options

[`AiAgentRunOptions`](../type-aliases/AiAgentRunOptions.md)

## Returns

`AsyncGenerator`\<[`AiStreamEvent`](../../../../api-shared/types/ai/type-aliases/AiStreamEvent.md)\>
