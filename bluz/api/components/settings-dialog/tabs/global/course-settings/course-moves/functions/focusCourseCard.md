[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/course-settings/course-moves](../index.md) / focusCourseCard

# Function: focusCourseCard()

> **focusCourseCard**(`courseId`): `void`

Defined in: [ui/src/components/settings-dialog/tabs/global/course-settings/course-moves.ts:53](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/settings-dialog/tabs/global/course-settings/course-moves.ts#L53)

Focuses a course's card once the tree has re-rendered after a move: the
card that held focus may have just unmounted under a collapsed parent.
CourseItem marks each card with `data-course-card`.

## Parameters

### courseId

`string`

## Returns

`void`
