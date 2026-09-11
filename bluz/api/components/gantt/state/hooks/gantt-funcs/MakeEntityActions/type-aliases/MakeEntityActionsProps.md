[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/state/hooks/gantt-funcs/MakeEntityActions](../index.md) / MakeEntityActionsProps

# Type Alias: MakeEntityActionsProps\<TEntity, TContainerId, TCreatePayload\>

> **MakeEntityActionsProps**\<`TEntity`, `TContainerId`, `TCreatePayload`\> = `object`

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:37](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L37)

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

### TContainerId

`TContainerId` *extends* [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)\[`"id"`\]

### TCreatePayload

`TCreatePayload`

## Properties

### api

> **api**: [`BasicGantApi`](../../../../../../../api-client/gantt/base/type-aliases/BasicGantApi.md)\<`TEntity`, `TCreatePayload`\>

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:42](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L42)

***

### builders

> **builders**: [`EntityActionBuilders`](EntityActionBuilders.md)\<`TEntity`, `TContainerId`\>

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:48](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L48)

***

### containerLabel

> **containerLabel**: `string`

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:47](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L47)

Container name used in link/unlink error messages, e.g. "syllabus".

***

### dispatch

> **dispatch**: `Dispatch`\<[`Action`](../../../../reducers/actions/type-aliases/Action.md)\>

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:43](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L43)

***

### getAllocatedTime?

> `optional` **getAllocatedTime?**: (`id`) => `number` \| `undefined`

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:67](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L67)

Reads the entity's current allocated duration. When provided,
`allocateTime` becomes optimistic and rolls back to this value on
failure.

Only supply it when `builders.allocateTime` maps to a *scalar* reducer
action. Events qualify (`ALLOCATE_TIME` writes one field); modules do
not — `ALLOCATE_TIME_TO_MODULE` redistributes time across every child
event, so restoring a single number would not undo it. Modules
therefore omit this and keep waiting on the server (#328).

#### Parameters

##### id

`TEntity`\[`"id"`\]

#### Returns

`number` \| `undefined`

***

### getEntity?

> `optional` **getEntity?**: (`id`) => `TEntity` \| `undefined`

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:55](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L55)

Reads the current entity from the store. When provided, `update` becomes
optimistic: it snapshots these values, dispatches immediately, and rolls
back on failure — like `updateWeek` (#327, #328). Must be stable (e.g. a
ref-backed useCallback) so the returned actions stay memoized.

#### Parameters

##### id

`TEntity`\[`"id"`\]

#### Returns

`TEntity` \| `undefined`

***

### label

> **label**: `string`

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:45](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L45)

Entity name used in error messages, e.g. "module".
