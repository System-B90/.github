[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/course-settings/CourseItemQuickActionControls](../index.md) / courseDeleteMessage

# Function: courseDeleteMessage()

> **courseDeleteMessage**(`name`, `subCourseCount`): `string`

Defined in: [ui/src/components/settings-dialog/tabs/global/course-settings/CourseItemQuickActionControls.tsx:30](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/settings-dialog/tabs/global/course-settings/CourseItemQuickActionControls.tsx#L30)

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
