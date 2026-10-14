[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/fixture](../index.md) / benchmarkTools

# Function: benchmarkTools()

> **benchmarkTools**(`production`): [`AiTool`](../../../tools/types/type-aliases/AiTool.md)\<`any`\>[]

Defined in: [ui/src/api-server/ai/benchmark/fixture.ts:619](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/ai/benchmark/fixture.ts#L619)

The tool surface a run offers: every production tool, by its production
name, description and schema, so tool choice is as hard as in real chat.

- A tool the fixture models answers from the fixture.
- Any other read answers "no data here" rather than touching real data.
- Every write can only be proposed, never run.
- Prompt tools (ask_user) are kept as they are.

Fixture tools with no production twin (tests mock the registry away) are
appended so the suite still runs.

## Parameters

### production

[`AiTool`](../../../tools/types/type-aliases/AiTool.md)\<`any`\>[]

## Returns

[`AiTool`](../../../tools/types/type-aliases/AiTool.md)\<`any`\>[]
