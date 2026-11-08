[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/iteration-request](../index.md) / ResolvedIteration

# Type Alias: ResolvedIteration

> **ResolvedIteration** = `object`

Defined in: [ui/src/api-server/iteration-request.ts:32](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/iteration-request.ts#L32)

## Properties

### controller

> **controller**: [`DatabaseController`](../../mongo-db-controller/classes/DatabaseController.md)

Defined in: [ui/src/api-server/iteration-request.ts:36](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/iteration-request.ts#L36)

Controller scoped to that iteration's database.

***

### iterationId?

> `optional` **iterationId?**: [`IterationId`](../../../api-shared/types/iteration/type-aliases/IterationId.md)

Defined in: [ui/src/api-server/iteration-request.ts:34](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/iteration-request.ts#L34)

The iteration id from the request, or undefined for the current run.
