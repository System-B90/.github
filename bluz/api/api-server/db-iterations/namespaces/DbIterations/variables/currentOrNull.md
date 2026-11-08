[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / currentOrNull

# Variable: currentOrNull

> `const` **currentOrNull**: () => `Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md) \| `null`\> = `getCurrentIterationOrNull`

Defined in: [ui/src/api-server/db-iterations.ts:452](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/db-iterations.ts#L452)

The current iteration, or null when the registry is still empty — a fresh
install before the user has created their first iteration (#471). Read paths
use this and prompt; write paths use [getCurrentIteration](current.md), which
refuses to guess.

## Returns

`Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md) \| `null`\>
