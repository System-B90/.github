[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/fixture](../index.md) / FIXTURE\_TOOLS

# Variable: FIXTURE\_TOOLS

> `const` **FIXTURE\_TOOLS**: [`AiTool`](../../../tools/types/type-aliases/AiTool.md)\<`any`\>[]

Defined in: [ui/src/api-server/ai/benchmark/fixture.ts:513](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-server/ai/benchmark/fixture.ts#L513)

The fixture's own tools. The run lays them over the production registry
(see `benchmarkTools`), so the model sees every real tool; these only
supply answers.
