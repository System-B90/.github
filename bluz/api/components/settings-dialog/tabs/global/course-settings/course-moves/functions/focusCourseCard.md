[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/course-settings/course-moves](../index.md) / focusCourseCard

# Function: focusCourseCard()

> **focusCourseCard**(`courseId`): `void`

Defined in: [ui/src/components/settings-dialog/tabs/global/course-settings/course-moves.ts:53](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/settings-dialog/tabs/global/course-settings/course-moves.ts#L53)

Focuses a course's card once the tree has re-rendered after a move: the
card that held focus may have just unmounted under a collapsed parent.
CourseItem marks each card with `data-course-card`.

## Parameters

### courseId

`string`

## Returns

`void`
