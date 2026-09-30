[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/offline-dialogs/push-updates-dialog/utils](../index.md) / pushSelectedCollisionUpdates

# Function: pushSelectedCollisionUpdates()

> **pushSelectedCollisionUpdates**(`collisionStates`, `selectedIds`, `api`): `Promise`\<[`PushOutcome`](../type-aliases/PushOutcome.md)\>

Defined in: [ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts:201](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts#L201)

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
