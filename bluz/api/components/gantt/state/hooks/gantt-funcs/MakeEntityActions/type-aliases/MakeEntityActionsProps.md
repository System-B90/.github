[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/state/hooks/gantt-funcs/MakeEntityActions](../index.md) / MakeEntityActionsProps

# Type Alias: MakeEntityActionsProps\<TEntity, TContainerId, TCreatePayload\>

> **MakeEntityActionsProps**\<`TEntity`, `TContainerId`, `TCreatePayload`\> = `object`

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:29](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L29)

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

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:34](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L34)

***

### builders

> **builders**: [`EntityActionBuilders`](EntityActionBuilders.md)\<`TEntity`, `TContainerId`\>

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:40](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L40)

***

### containerLabel

> **containerLabel**: `string`

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:39](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L39)

Container name used in link/unlink error messages, e.g. "syllabus".

***

### dispatch

> **dispatch**: `Dispatch`\<[`Action`](../../../../reducers/actions/type-aliases/Action.md)\>

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:35](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L35)

***

### getEntity?

> `optional` **getEntity?**: (`id`) => `TEntity` \| `undefined`

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:47](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L47)

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

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:37](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L37)

Entity name used in error messages, e.g. "module".
