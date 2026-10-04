[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/collapse-course-selection](../index.md) / collapseCourseSelection

# Function: collapseCourseSelection()

> **collapseCourseSelection**(`selectedIds`, `allCourses`): [`Course`](../../../../api-shared/types/course/type-aliases/Course.md)[]

Defined in: [ui/src/components/base/collapse-course-selection.ts:15](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/base/collapse-course-selection.ts#L15)

Collapses a flat course selection up the course tree.

A course counts as "covered" when it is selected itself, or when it has
children and every one of them is covered. Only the highest covered course of
each branch is returned, so selecting every child of a parent displays the
parent alone, and selecting every course displays the roots alone.

## Parameters

### selectedIds

readonly `string`[]

The ids selected on the event.

### allCourses

readonly [`Course`](../../../../api-shared/types/course/type-aliases/Course.md)[]

Every known course, used to rebuild the tree.

## Returns

[`Course`](../../../../api-shared/types/course/type-aliases/Course.md)[]

The courses to display, in `allCourses` order.
