[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/offline-dialogs/push-updates-dialog/utils](../index.md) / reconcileCollisionStatesAfterPush

# Function: reconcileCollisionStatesAfterPush()

> **reconcileCollisionStatesAfterPush**(`collisionStates`, `resolvedIds`): [`CollisionStates`](../../types/type-aliases/CollisionStates.md)

Defined in: [ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts:262](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts#L262)

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
