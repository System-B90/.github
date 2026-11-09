[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/fixture](../index.md) / FIXTURE\_TOOLS

# Variable: FIXTURE\_TOOLS

> `const` **FIXTURE\_TOOLS**: [`AiTool`](../../../tools/types/type-aliases/AiTool.md)\<`any`\>[]

Defined in: [ui/src/api-server/ai/benchmark/fixture.ts:513](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/ai/benchmark/fixture.ts#L513)

The fixture's own tools. The run lays them over the production registry
(see `benchmarkTools`), so the model sees every real tool; these only
supply answers.
