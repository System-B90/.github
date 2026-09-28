[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / getByCurriculum

# Variable: getByCurriculum

> `const` **getByCurriculum**: (`curriculumId`) => `Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md) \| `null`\> = `getIterationByCurriculum`

Defined in: [ui/src/api-server/db-iterations.ts:380](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-server/db-iterations.ts#L380)

Find the iteration linked to a given Postgres curriculum, i.e. the iteration
whose `ganttCurriculumId` equals `curriculumId`. Used by the curriculum cut
(#118) to locate the target schedule database. Returns null when nothing is
linked.

## Parameters

### curriculumId

`string`

## Returns

`Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md) \| `null`\>
