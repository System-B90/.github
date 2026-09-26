[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/module-dialog/constraints/use-constraint-editor](../index.md) / useConstraintEditor

# Function: useConstraintEditor()

> **useConstraintEditor**(`ownerType`, `ownerId`): `object`

Defined in: [ui/src/components/gantt/module-dialog/constraints/use-constraint-editor.ts:91](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/module-dialog/constraints/use-constraint-editor.ts#L91)

Create/edit/remove state machine shared by the module- and event-level
constraint panels. The only difference between the two is the owner fields
stamped onto the create payload and which constraints are listed.

## Parameters

### ownerType

[`ConstraintOwnerType`](../type-aliases/ConstraintOwnerType.md)

### ownerId

`string`

## Returns

`object`

### cancelCreate

> **cancelCreate**: () => `void`

#### Returns

`void`

### cancelEdit

> **cancelEdit**: () => `void`

#### Returns

`void`

### constraints

> **constraints**: [`GanttConstraint`](../../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]

### draft

> **draft**: [`DraftConstraint`](../../types/type-aliases/DraftConstraint.md) \| `null`

### editingConstraintId

> **editingConstraintId**: `string` \| `null`

### editingDraft

> **editingDraft**: [`DraftConstraint`](../../types/type-aliases/DraftConstraint.md) \| `null`

### hasTemporalConflict

> **hasTemporalConflict**: `boolean`

### isLoading

> **isLoading**: `boolean` = `state.isLoading`

### removeConstraint

> **removeConstraint**: [`RemoveConstraint`](../../../../state/constraints/context/type-aliases/RemoveConstraint.md)

### setDraft

> **setDraft**: `Dispatch`\<`SetStateAction`\<[`DraftConstraint`](../../types/type-aliases/DraftConstraint.md) \| `null`\>\>

### setEditingDraft

> **setEditingDraft**: `Dispatch`\<`SetStateAction`\<[`DraftConstraint`](../../types/type-aliases/DraftConstraint.md) \| `null`\>\>

### startCreate

> **startCreate**: () => `void`

#### Returns

`void`

### startEdit

> **startEdit**: (`constraint`) => `void`

#### Parameters

##### constraint

[`GanttConstraint`](../../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)

#### Returns

`void`

### submitCreate

> **submitCreate**: () => `Promise`\<`void`\>

#### Returns

`Promise`\<`void`\>

### submitEdit

> **submitEdit**: () => `Promise`\<`void`\>

#### Returns

`Promise`\<`void`\>
