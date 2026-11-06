[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/offline-dialogs/push-updates-dialog/utils](../index.md) / reconcileCollisionStatesAfterPush

# Function: reconcileCollisionStatesAfterPush()

> **reconcileCollisionStatesAfterPush**(`collisionStates`, `resolvedIds`): [`CollisionStates`](../../types/type-aliases/CollisionStates.md)

Defined in: [ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts:250](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts#L250)

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
