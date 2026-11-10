[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/offline-dialogs/push-updates-dialog/utils](../index.md) / pushSelectedCollisionUpdates

# Function: pushSelectedCollisionUpdates()

> **pushSelectedCollisionUpdates**(`collisionStates`, `selectedIds`, `api`): `Promise`\<[`PushOutcome`](../type-aliases/PushOutcome.md)\>

Defined in: [ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts:209](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts#L209)

Pushes the selected offline edits to the server one at a time, isolating
each write in its own try/catch (#157). A failure mid-loop no longer aborts
the whole batch: earlier items that already committed are reported as
succeeded and the remaining items keep going, so only genuinely-failed items
stay pending. Returns the per-event outcome for reconciliation.

## Parameters

### collisionStates

[`CollisionStates`](../../types/type-aliases/CollisionStates.md)

### selectedIds

`string`[]

### api

[`PushApi`](../type-aliases/PushApi.md)

## Returns

`Promise`\<[`PushOutcome`](../type-aliases/PushOutcome.md)\>
