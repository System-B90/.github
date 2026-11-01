[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/course-settings/CourseItemQuickActionControls](../index.md) / courseDeleteMessage

# Function: courseDeleteMessage()

> **courseDeleteMessage**(`name`, `subCourseCount`): `string`

Defined in: [ui/src/components/settings-dialog/tabs/global/course-settings/CourseItemQuickActionControls.tsx:30](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/settings-dialog/tabs/global/course-settings/CourseItemQuickActionControls.tsx#L30)

A course is shared, server-side and has no undo, so deleting it confirms
by name. Its sub-courses survive the delete but lose their parent, which
moves them to the top of the tree — the prompt says so.

## Parameters

### name

`string`

### subCourseCount

`number`

## Returns

`string`
