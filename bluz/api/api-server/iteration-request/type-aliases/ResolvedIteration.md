[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/iteration-request](../index.md) / ResolvedIteration

# Type Alias: ResolvedIteration

> **ResolvedIteration** = `object`

Defined in: [ui/src/api-server/iteration-request.ts:31](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/iteration-request.ts#L31)

## Properties

### controller

> **controller**: [`DatabaseController`](../../mongo-db-controller/classes/DatabaseController.md)

Defined in: [ui/src/api-server/iteration-request.ts:35](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/iteration-request.ts#L35)

Controller scoped to that iteration's database.

***

### iterationId?

> `optional` **iterationId?**: [`IterationId`](../../../api-shared/types/iteration/type-aliases/IterationId.md)

Defined in: [ui/src/api-server/iteration-request.ts:33](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/iteration-request.ts#L33)

The iteration id from the request, or undefined for the current run.
