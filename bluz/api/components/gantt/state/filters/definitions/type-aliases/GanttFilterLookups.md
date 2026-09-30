[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/filters/definitions](../index.md) / GanttFilterLookups

# Type Alias: GanttFilterLookups

> **GanttFilterLookups** = `object`

Defined in: [ui/src/components/gantt/state/filters/definitions.ts:13](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/state/filters/definitions.ts#L13)

Lookups the filter descriptions need to turn ids into names.

## Properties

### getCourse

> **getCourse**: (`id`) => [`Course`](../../../../../../api-shared/types/course/type-aliases/Course.md) \| `undefined`

Defined in: [ui/src/components/gantt/state/filters/definitions.ts:14](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/state/filters/definitions.ts#L14)

#### Parameters

##### id

[`CourseId`](../../../../../../api-shared/types/course/type-aliases/CourseId.md)

#### Returns

[`Course`](../../../../../../api-shared/types/course/type-aliases/Course.md) \| `undefined`

***

### getInstructor

> **getInstructor**: (`id`) => `CourseUser` \| `undefined`

Defined in: [ui/src/components/gantt/state/filters/definitions.ts:15](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/state/filters/definitions.ts#L15)

#### Parameters

##### id

`number`

#### Returns

`CourseUser` \| `undefined`
