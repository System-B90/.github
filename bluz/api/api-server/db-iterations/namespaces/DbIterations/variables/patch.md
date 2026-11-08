[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / patch

# Variable: patch

> `const` **patch**: (`id`, `patch`) => `Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md)\> = `patchIteration`

Defined in: [ui/src/api-server/db-iterations.ts:457](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/db-iterations.ts#L457)

Patch an iteration. Setting `isCurrent: true` atomically demotes whichever
iteration was previously current, so exactly one stays current.

## Parameters

### id

`string`

### patch

[`PatchIterationPayload`](../../../../../api-shared/types/iteration/type-aliases/PatchIterationPayload.md)

## Returns

`Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md)\>
