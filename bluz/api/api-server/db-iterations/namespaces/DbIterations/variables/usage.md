[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / usage

# Variable: usage

> `const` **usage**: (`id`) => `Promise`\<[`IterationUsage`](../../../../../api-shared/types/iteration/type-aliases/IterationUsage.md)\> = `describeIterationUsage`

Defined in: [ui/src/api-server/db-iterations.ts:453](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/db-iterations.ts#L453)

What still hangs off an iteration. Only a fully orphaned iteration may be
deleted (#473), so the UI asks for this to decide whether to enable its
delete button rather than letting the user discover the rule from an error.

## Parameters

### id

`string`

## Returns

`Promise`\<[`IterationUsage`](../../../../../api-shared/types/iteration/type-aliases/IterationUsage.md)\>
