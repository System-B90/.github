[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / patch

# Variable: patch

> `const` **patch**: (`id`, `patch`) => `Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md)\> = `patchIteration`

Defined in: [ui/src/api-server/db-iterations.ts:382](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/db-iterations.ts#L382)

Patch an iteration. Setting `isCurrent: true` atomically demotes whichever
iteration was previously current, so exactly one stays current.

## Parameters

### id

`string`

### patch

[`PatchIterationPayload`](../../../../../api-shared/types/iteration/type-aliases/PatchIterationPayload.md)

## Returns

`Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md)\>
