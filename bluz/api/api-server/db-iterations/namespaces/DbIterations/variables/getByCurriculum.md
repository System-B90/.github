[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / getByCurriculum

# Variable: getByCurriculum

> `const` **getByCurriculum**: (`curriculumId`) => `Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md) \| `null`\> = `getIterationByCurriculum`

Defined in: [ui/src/api-server/db-iterations.ts:455](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/db-iterations.ts#L455)

Find the iteration linked to a given Postgres curriculum, i.e. the iteration
whose `ganttCurriculumId` equals `curriculumId`. Used by the curriculum cut
(#118) to locate the target schedule database. Returns null when nothing is
linked.

## Parameters

### curriculumId

`string`

## Returns

`Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md) \| `null`\>
