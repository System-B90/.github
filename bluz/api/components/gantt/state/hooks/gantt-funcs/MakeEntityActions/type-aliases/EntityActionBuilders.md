[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/state/hooks/gantt-funcs/MakeEntityActions](../index.md) / EntityActionBuilders

# Type Alias: EntityActionBuilders\<TEntity, TContainerId\>

> **EntityActionBuilders**\<`TEntity`, `TContainerId`\> = `object`

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:14](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L14)

Per-entity dispatch builders. Payload key names differ per entity
(e.g. ADD_MODULE carries `{ module, syllabusId }` while ADD_EVENT carries
`{ event, moduleId }`), so each hook maps the generic call into its
reducer action here.

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

### TContainerId

`TContainerId` *extends* [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)\[`"id"`\]

## Properties

### add

> **add**: (`entity`, `containerId`) => [`Action`](../../../../reducers/actions/type-aliases/Action.md)

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:18](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L18)

#### Parameters

##### entity

`TEntity`

##### containerId

`TContainerId`

#### Returns

[`Action`](../../../../reducers/actions/type-aliases/Action.md)

***

### discard?

> `optional` **discard?**: (`id`) => [`Action`](../../../../reducers/actions/type-aliases/Action.md)

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:26](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L26)

Deletes a doc outright rather than unlinking it from `containerId`
(unlike `remove`). Used to undo an optimistic `create` by discarding
its temp entity — see `create`'s `buildOptimistic` parameter (#381).

#### Parameters

##### id

`TEntity`\[`"id"`\]

#### Returns

[`Action`](../../../../reducers/actions/type-aliases/Action.md)

***

### remove

> **remove**: (`containerId`, `id`) => [`Action`](../../../../reducers/actions/type-aliases/Action.md)

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:20](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L20)

#### Parameters

##### containerId

`TContainerId`

##### id

`TEntity`\[`"id"`\]

#### Returns

[`Action`](../../../../reducers/actions/type-aliases/Action.md)

***

### update

> **update**: (`id`, `updates`) => [`Action`](../../../../reducers/actions/type-aliases/Action.md)

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:19](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L19)

#### Parameters

##### id

`TEntity`\[`"id"`\]

##### updates

`Partial`\<`TEntity`\>

#### Returns

[`Action`](../../../../reducers/actions/type-aliases/Action.md)
