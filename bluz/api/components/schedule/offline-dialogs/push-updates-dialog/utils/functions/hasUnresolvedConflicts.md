[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/offline-dialogs/push-updates-dialog/utils](../index.md) / hasUnresolvedConflicts

# Function: hasUnresolvedConflicts()

> **hasUnresolvedConflicts**(`collisionStates`, `selectedIds`): `boolean`

Defined in: [ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts:147](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts#L147)

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
