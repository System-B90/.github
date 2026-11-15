[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-drag](../index.md) / planModuleShift

# Function: planModuleShift()

> **planModuleShift**(`mappings`, `linearDays`, `deltaDays`): [`MappingMove`](../type-aliases/MappingMove.md)[] \| `null`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-drag.ts:52](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-drag.ts#L52)

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
