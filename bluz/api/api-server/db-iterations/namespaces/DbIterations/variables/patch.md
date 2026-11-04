[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / patch

# Variable: patch

> `const` **patch**: (`id`, `patch`) => `Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md)\> = `patchIteration`

Defined in: [ui/src/api-server/db-iterations.ts:457](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/db-iterations.ts#L457)

Patch an iteration. Setting `isCurrent: true` atomically demotes whichever
iteration was previously current, so exactly one stays current.

## Parameters

### id

`string`

### patch

[`PatchIterationPayload`](../../../../../api-shared/types/iteration/type-aliases/PatchIterationPayload.md)

## Returns

`Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md)\>
