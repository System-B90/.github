[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-drag](../index.md) / planModuleShift

# Function: planModuleShift()

> **planModuleShift**(`mappings`, `linearDays`, `deltaDays`): [`MappingMove`](../type-aliases/MappingMove.md)[] \| `null`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-drag.ts:52](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-drag.ts#L52)

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
