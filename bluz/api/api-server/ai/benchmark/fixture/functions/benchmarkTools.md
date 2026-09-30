[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/fixture](../index.md) / benchmarkTools

# Function: benchmarkTools()

> **benchmarkTools**(`production`): [`AiTool`](../../../tools/types/type-aliases/AiTool.md)\<`any`\>[]

Defined in: [ui/src/api-server/ai/benchmark/fixture.ts:625](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/ai/benchmark/fixture.ts#L625)

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
