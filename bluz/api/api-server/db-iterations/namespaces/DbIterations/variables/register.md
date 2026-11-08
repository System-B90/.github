[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / register

# Variable: register

> `const` **register**: (`payload`) => `Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md)\> = `registerIteration`

Defined in: [ui/src/api-server/db-iterations.ts:456](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/db-iterations.ts#L456)

Register a new iteration and lazily provision its database. Mongo creates the
database on first write, so no explicit creation is needed here.

## Parameters

### payload

[`RegisterIterationPayload`](../../../../../api-shared/types/iteration/type-aliases/RegisterIterationPayload.md)

## Returns

`Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md)\>
