[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/course-settings/course-moves](../index.md) / wouldNestInsideItself

# Function: wouldNestInsideItself()

> **wouldNestInsideItself**(`courses`, `movingId`, `targetId`): `boolean`

Defined in: [ui/src/components/settings-dialog/tabs/global/course-settings/course-moves.ts:10](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/settings-dialog/tabs/global/course-settings/course-moves.ts#L10)

Whether making `targetId` the parent of `movingId` would put the course
inside itself: the target is the course or one of its descendants.
Shared by the drag drop and the move menu (#885). Cycles in the data are
safe.

## Parameters

### courses

readonly [`Course`](../../../../../../../api-shared/types/course/type-aliases/Course.md)[]

### movingId

`string`

### targetId

`string`

## Returns

`boolean`
