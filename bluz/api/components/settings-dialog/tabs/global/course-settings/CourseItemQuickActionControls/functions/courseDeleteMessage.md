[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/course-settings/CourseItemQuickActionControls](../index.md) / courseDeleteMessage

# Function: courseDeleteMessage()

> **courseDeleteMessage**(`name`, `subCourseCount`): `string`

Defined in: [ui/src/components/settings-dialog/tabs/global/course-settings/CourseItemQuickActionControls.tsx:30](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/settings-dialog/tabs/global/course-settings/CourseItemQuickActionControls.tsx#L30)

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
