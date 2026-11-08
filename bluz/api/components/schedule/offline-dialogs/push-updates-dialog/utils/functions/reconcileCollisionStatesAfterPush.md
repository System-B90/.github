[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/offline-dialogs/push-updates-dialog/utils](../index.md) / reconcileCollisionStatesAfterPush

# Function: reconcileCollisionStatesAfterPush()

> **reconcileCollisionStatesAfterPush**(`collisionStates`, `resolvedIds`): [`CollisionStates`](../../types/type-aliases/CollisionStates.md)

Defined in: [ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts:262](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts#L262)

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
