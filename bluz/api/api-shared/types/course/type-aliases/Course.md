[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/course](../index.md) / Course

# Type Alias: Course

> **Course** = `object`

Defined in: [ui/src/api-shared/types/course.ts:4](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/course.ts#L4)

## Properties

### color

> **color**: [`Color`](../../../common/type-aliases/Color.md) \| `null`

Defined in: [ui/src/api-shared/types/course.ts:7](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/course.ts#L7)

***

### description?

> `optional` **description?**: `string`

Defined in: [ui/src/api-shared/types/course.ts:11](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/course.ts#L11)

Optional free-text description (e.g. provenance of auto-created courses).

***

### hiveClassId?

> `optional` **hiveClassId?**: `null` \| `number`

Defined in: [ui/src/api-shared/types/course.ts:16](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/course.ts#L16)

Hive student group this course (a shuffle) is explicitly linked to
(#774). Unset ⇒ matched to the Hive group with the same name.

***

### id

> **id**: [`CourseId`](CourseId.md)

Defined in: [ui/src/api-shared/types/course.ts:5](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/course.ts#L5)

***

### instructorIds?

> `optional` **instructorIds?**: `number`[]

Defined in: [ui/src/api-shared/types/course.ts:9](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/course.ts#L9)

***

### name

> **name**: `string`

Defined in: [ui/src/api-shared/types/course.ts:6](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/course.ts#L6)

***

### parentId?

> `optional` **parentId?**: `null` \| `string`

Defined in: [ui/src/api-shared/types/course.ts:8](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/course.ts#L8)
