[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/constraints/context](../index.md) / CreateConstraint

# Type Alias: CreateConstraint

> **CreateConstraint** = (`payload`) => `Promise`\<[`GanttConstraint`](../../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md) \| `undefined`\>

Defined in: [ui/src/components/gantt/state/constraints/context.ts:18](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/state/constraints/context.ts#L18)

Type signature for the function that creates a new constraint.

## Parameters

### payload

`Omit`\<[`CreateConstraintPayload`](../../../../../../api-shared/types/gantt/create-payloads/type-aliases/CreateConstraintPayload.md), `"id"`\>

The constraint details excluding its ID.

## Returns

`Promise`\<[`GanttConstraint`](../../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md) \| `undefined`\>

The created constraint or undefined if creation failed.
