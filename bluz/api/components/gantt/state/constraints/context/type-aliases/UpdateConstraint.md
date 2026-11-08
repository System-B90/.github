[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/constraints/context](../index.md) / UpdateConstraint

# Type Alias: UpdateConstraint

> **UpdateConstraint** = (`id`, `payload`) => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/state/constraints/context.ts:28](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/state/constraints/context.ts#L28)

Type signature for the function that updates an existing constraint.

## Parameters

### id

`string`

The unique constraint identifier.

### payload

`Partial`\<[`CreateConstraintPayload`](../../../../../../api-shared/types/gantt/create-payloads/type-aliases/CreateConstraintPayload.md)\>

The fields to update.

## Returns

`Promise`\<`void`\>
