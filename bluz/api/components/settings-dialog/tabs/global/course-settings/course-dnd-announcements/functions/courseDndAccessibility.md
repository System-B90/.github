[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/course-settings/course-dnd-announcements](../index.md) / courseDndAccessibility

# Function: courseDndAccessibility()

> **courseDndAccessibility**(`courses`, `instructors`): `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/course-settings/course-dnd-announcements.ts:15](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/settings-dialog/tabs/global/course-settings/course-dnd-announcements.ts#L15)

Hebrew screen-reader text for the course builder's drag and drop (#885).
dnd-kit's defaults are English and name items by their internal ids.
Worded without gendered verbs: the item may be a course or an instructor.

## Parameters

### courses

readonly [`Course`](../../../../../../../api-shared/types/course/type-aliases/Course.md)[]

### instructors

readonly `CourseUser`[]

## Returns

`object`

### announcements

> **announcements**: `Announcements`

### screenReaderInstructions

> **screenReaderInstructions**: `ScreenReaderInstructions`
