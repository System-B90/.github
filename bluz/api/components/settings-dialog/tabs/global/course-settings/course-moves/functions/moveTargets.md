[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/course-settings/course-moves](../index.md) / moveTargets

# Function: moveTargets()

> **moveTargets**(`courses`, `course`, `searchQuery?`): [`CourseOption`](../../../../../../base/course-options/type-aliases/CourseOption.md)[]

Defined in: [ui/src/components/settings-dialog/tabs/global/course-settings/course-moves.ts:33](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/settings-dialog/tabs/global/course-settings/course-moves.ts#L33)

Where `course` can move to, as course-tree rows: every course except the
course itself, its descendants (which would make a cycle) and its current
parent (a no-op). A search keeps matches plus their ancestors.

## Parameters

### courses

readonly [`Course`](../../../../../../../api-shared/types/course/type-aliases/Course.md)[]

### course

[`Course`](../../../../../../../api-shared/types/course/type-aliases/Course.md)

### searchQuery?

`string` = `""`

## Returns

[`CourseOption`](../../../../../../base/course-options/type-aliases/CourseOption.md)[]
