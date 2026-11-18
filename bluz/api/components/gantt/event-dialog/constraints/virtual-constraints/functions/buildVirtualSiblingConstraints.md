[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/event-dialog/constraints/virtual-constraints](../index.md) / buildVirtualSiblingConstraints

# Function: buildVirtualSiblingConstraints()

> **buildVirtualSiblingConstraints**(`eventId`, `moduleId`, `moduleEvents`): [`RelationalConstraint`](../../../../../../api-shared/types/gantt/models/constraint/type-aliases/RelationalConstraint.md)[]

Defined in: [ui/src/components/gantt/event-dialog/constraints/virtual-constraints.ts:9](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/gantt/event-dialog/constraints/virtual-constraints.ts#L9)

Derives read-only sibling ordering constraints from the event's position
in the module's event list. These are never persisted — they reflect the
current ordering and should update when events are reordered.

## Parameters

### eventId

`string`

### moduleId

`string`

### moduleEvents

`string`[]

## Returns

[`RelationalConstraint`](../../../../../../api-shared/types/gantt/models/constraint/type-aliases/RelationalConstraint.md)[]
