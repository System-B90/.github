[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/course-options](../index.md) / buildCourseOptions

# Function: buildCourseOptions()

> **buildCourseOptions**(`courses`, `__namedParameters?`): [`CourseOption`](../type-aliases/CourseOption.md)[]

Defined in: [ui/src/components/base/course-options.ts:29](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/course-options.ts#L29)

Flattens the course tree into select rows in depth-first order, siblings
sorted by Hebrew name.

Hidden shuffle-courses lift their visible descendants up to the nearest
visible ancestor, so hiding a shuffle never hides a regular course. A search
keeps matching courses plus their ancestors (flagged `contextOnly`), so a
match always shows where it sits in the tree. Cycles are safe.

## Parameters

### courses

readonly [`Course`](../../../../api-shared/types/course/type-aliases/Course.md)[]

### \_\_namedParameters?

[`CourseOptionsFilter`](../type-aliases/CourseOptionsFilter.md) = `{}`

## Returns

[`CourseOption`](../type-aliases/CourseOption.md)[]
