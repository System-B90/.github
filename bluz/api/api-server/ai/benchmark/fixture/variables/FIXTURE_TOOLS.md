[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/fixture](../index.md) / FIXTURE\_TOOLS

# Variable: FIXTURE\_TOOLS

> `const` **FIXTURE\_TOOLS**: [`AiTool`](../../../tools/types/type-aliases/AiTool.md)\<`any`\>[]

Defined in: [ui/src/api-server/ai/benchmark/fixture.ts:504](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/ai/benchmark/fixture.ts#L504)

The fixture's own tools. The run lays them over the production registry
(see `benchmarkTools`), so the model sees every real tool; these only
supply answers.
