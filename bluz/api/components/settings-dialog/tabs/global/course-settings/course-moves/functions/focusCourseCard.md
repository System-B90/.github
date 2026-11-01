[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/course-settings/course-moves](../index.md) / focusCourseCard

# Function: focusCourseCard()

> **focusCourseCard**(`courseId`): `void`

Defined in: [ui/src/components/settings-dialog/tabs/global/course-settings/course-moves.ts:53](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/settings-dialog/tabs/global/course-settings/course-moves.ts#L53)

Focuses a course's card once the tree has re-rendered after a move: the
card that held focus may have just unmounted under a collapsed parent.
CourseItem marks each card with `data-course-card`.

## Parameters

### courseId

`string`

## Returns

`void`
