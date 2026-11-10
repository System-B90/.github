[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/constraints/context](../index.md) / UpdateConstraint

# Type Alias: UpdateConstraint

> **UpdateConstraint** = (`id`, `payload`) => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/state/constraints/context.ts:28](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/state/constraints/context.ts#L28)

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
