[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/offline-dialogs/push-updates-dialog/utils](../index.md) / reconcileCollisionStatesAfterPush

# Function: reconcileCollisionStatesAfterPush()

> **reconcileCollisionStatesAfterPush**(`collisionStates`, `resolvedIds`): [`CollisionStates`](../../types/type-aliases/CollisionStates.md)

Defined in: [ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts:238](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts#L238)

Removes already-resolved events (synced or reverted) from the collision set
so a partial-failure retry only re-shows the items that still need syncing
(#157).

## Parameters

### collisionStates

[`CollisionStates`](../../types/type-aliases/CollisionStates.md)

### resolvedIds

`string`[]

## Returns

[`CollisionStates`](../../types/type-aliases/CollisionStates.md)
