[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/course-settings/course-moves](../index.md) / focusCourseCard

# Function: focusCourseCard()

> **focusCourseCard**(`courseId`): `void`

Defined in: [ui/src/components/settings-dialog/tabs/global/course-settings/course-moves.ts:52](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/settings-dialog/tabs/global/course-settings/course-moves.ts#L52)

Focuses a course's card once the tree has re-rendered after a move: the
card that held focus may have just unmounted under a collapsed parent.
CourseItem marks each card with `data-course-card`.

## Parameters

### courseId

`string`

## Returns

`void`
