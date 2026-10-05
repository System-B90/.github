[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-drag](../index.md) / planModuleShift

# Function: planModuleShift()

> **planModuleShift**(`mappings`, `linearDays`, `deltaDays`): [`MappingMove`](../type-aliases/MappingMove.md)[] \| `null`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-drag.ts:49](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-drag.ts#L49)

Moves every mapping by `deltaDays`, keeping their relative spacing.
All-or-nothing: `null` when any would leave the timeline. Ordered leading
edge first, so no move lands on a day a sibling still occupies.

## Parameters

### mappings

[`ModuleMapping`](../type-aliases/ModuleMapping.md)[]

### linearDays

`string`[]

### deltaDays

`number`

## Returns

[`MappingMove`](../type-aliases/MappingMove.md)[] \| `null`
