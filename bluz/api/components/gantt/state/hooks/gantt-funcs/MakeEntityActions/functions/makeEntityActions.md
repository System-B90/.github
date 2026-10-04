[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/state/hooks/gantt-funcs/MakeEntityActions](../index.md) / makeEntityActions

# Function: makeEntityActions()

> **makeEntityActions**\<`TEntity`, `TContainerId`, `TCreatePayload`\>(`__namedParameters`): `object`

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx:56](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/gantt/state/hooks/gantt-funcs/MakeEntityActions.tsx#L56)

Factors the "call gantt API → dispatch reducer action" pattern shared by the
module/syllabus/event action hooks (#190) so behavior fixes land in one
place. Entity-specific flows (optimistic week updates, event move/duplicate,
create-payload defaults) stay in their hooks.

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

### TContainerId

`TContainerId` *extends* `string`

### TCreatePayload

`TCreatePayload`

## Parameters

### \_\_namedParameters

[`MakeEntityActionsProps`](../type-aliases/MakeEntityActionsProps.md)\<`TEntity`, `TContainerId`, `TCreatePayload`\>

## Returns

### create

> **create**: (`payload`, `containerId`, `buildOptimistic?`) => `Promise`\<`TEntity` & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>

#### Parameters

##### payload

`TCreatePayload`

##### containerId

`TContainerId`

##### buildOptimistic?

(`tempId`) => `TEntity`

When given (together with `builders.discard`), `create` becomes
optimistic: it renders a temp entity immediately, then on success
discards the temp doc and adds the real one, or on failure just
discards it — mirroring `createWeek`'s temp-id + swap pattern
(#381). Without it, `create` stays non-optimistic: wait for the
API, then add the real entity.

#### Returns

`Promise`\<`TEntity` & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>

### link

> **link**: (`containerId`, `id`) => `Promise`\<`TEntity` & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>

#### Parameters

##### containerId

`TContainerId`

##### id

`TEntity`\[`"id"`\]

#### Returns

`Promise`\<`TEntity` & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>

### remove

> **remove**: (`containerId`, `id`) => `Promise`\<`void`\>

#### Parameters

##### containerId

`TContainerId`

##### id

`TEntity`\[`"id"`\]

#### Returns

`Promise`\<`void`\>

### unlink

> **unlink**: (`containerId`, `id`) => `Promise`\<`void`\>

#### Parameters

##### containerId

`TContainerId`

##### id

`TEntity`\[`"id"`\]

#### Returns

`Promise`\<`void`\>

### update

> **update**: (`id`, `updates`) => `Promise`\<`TEntity` & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>

#### Parameters

##### id

`TEntity`\[`"id"`\]

##### updates

`Partial`\<`TEntity`\>

#### Returns

`Promise`\<`TEntity` & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>
