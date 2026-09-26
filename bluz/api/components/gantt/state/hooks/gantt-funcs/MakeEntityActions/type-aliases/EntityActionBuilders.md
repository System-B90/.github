[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/state/hooks/gantt-funcs/MakeEntityActions](../index.md) / EntityActionBuilders

# Type Alias: EntityActionBuilders\<TEntity, TContainerId\>

> **EntityActionBuilders**\<`TEntity`, `TContainerId`\> = `object`

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:17](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L17)

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

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:21](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L21)

#### Parameters

##### entity

`TEntity`

##### containerId

`TContainerId`

#### Returns

[`Action`](../../../../reducers/actions/type-aliases/Action.md)

***

### allocateTime?

> `optional` **allocateTime?**: (`id`, `curriculumId`, `duration`) => [`Action`](../../../../reducers/actions/type-aliases/Action.md)

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:30](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L30)

#### Parameters

##### id

`TEntity`\[`"id"`\]

##### curriculumId

[`GanttCurriculumId`](../../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md)

##### duration

`number`

#### Returns

[`Action`](../../../../reducers/actions/type-aliases/Action.md)

***

### discard?

> `optional` **discard?**: (`id`) => [`Action`](../../../../reducers/actions/type-aliases/Action.md)

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:29](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L29)

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

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:23](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L23)

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

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:22](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L22)

#### Parameters

##### id

`TEntity`\[`"id"`\]

##### updates

`Partial`\<`TEntity`\>

#### Returns

[`Action`](../../../../reducers/actions/type-aliases/Action.md)
