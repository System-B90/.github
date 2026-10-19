[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/course-settings/course-moves](../index.md) / moveTargets

# Function: moveTargets()

> **moveTargets**(`courses`, `course`): [`CourseOption`](../../../../../../base/course-options/type-aliases/CourseOption.md)[]

Defined in: [ui/src/components/settings-dialog/tabs/global/course-settings/course-moves.ts:33](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/settings-dialog/tabs/global/course-settings/course-moves.ts#L33)

Where `course` can move to, as course-tree rows: every course except the
course itself, its descendants (which would make a cycle) and its current
parent (a no-op).

## Parameters

### courses

readonly [`Course`](../../../../../../../api-shared/types/course/type-aliases/Course.md)[]

### course

[`Course`](../../../../../../../api-shared/types/course/type-aliases/Course.md)

## Returns

[`CourseOption`](../../../../../../base/course-options/type-aliases/CourseOption.md)[]
