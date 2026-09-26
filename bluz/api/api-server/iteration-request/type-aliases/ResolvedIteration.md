[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/iteration-request](../index.md) / ResolvedIteration

# Type Alias: ResolvedIteration

> **ResolvedIteration** = `object`

Defined in: [ui/src/api-server/iteration-request.ts:31](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/iteration-request.ts#L31)

## Properties

### controller

> **controller**: [`DatabaseController`](../../mongo-db-controller/classes/DatabaseController.md)

Defined in: [ui/src/api-server/iteration-request.ts:35](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/iteration-request.ts#L35)

Controller scoped to that iteration's database.

***

### iterationId?

> `optional` **iterationId?**: [`IterationId`](../../../api-shared/types/iteration/type-aliases/IterationId.md)

Defined in: [ui/src/api-server/iteration-request.ts:33](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/iteration-request.ts#L33)

The iteration id from the request, or undefined for the current run.
