[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/offline-dialogs/push-updates-dialog/utils](../index.md) / hasUnresolvedConflicts

# Function: hasUnresolvedConflicts()

> **hasUnresolvedConflicts**(`collisionStates`, `selectedIds`): `boolean`

Defined in: [ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts:151](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts#L151)

True when the collision set has at least one real conflict (both captured
and server versions exist and differ) but none of those conflicting events
are currently selected — i.e. saving would be equivalent to accepting the
remote version for every conflict.

## Parameters

### collisionStates

[`CollisionStates`](../../types/type-aliases/CollisionStates.md)

### selectedIds

`string`[]

## Returns

`boolean`
