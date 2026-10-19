[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/agent](../index.md) / runAiAgent

# Function: runAiAgent()

> **runAiAgent**(`options`): `AsyncGenerator`\<[`AiStreamEvent`](../../../../api-shared/types/ai/type-aliases/AiStreamEvent.md)\>

Defined in: [ui/src/api-server/ai/agent.ts:138](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/ai/agent.ts#L138)

Runs one turn and yields it as a stream of app-level events.

The turn ends when the model stops calling tools, when a write needs
approval, when the model asks the human a question, or when
[AI\_MAX\_TOOL\_ITERATIONS](../../../../api-shared/types/ai/variables/AI_MAX_TOOL_ITERATIONS.md) is hit.

## Parameters

### options

[`AiAgentRunOptions`](../type-aliases/AiAgentRunOptions.md)

## Returns

`AsyncGenerator`\<[`AiStreamEvent`](../../../../api-shared/types/ai/type-aliases/AiStreamEvent.md)\>
