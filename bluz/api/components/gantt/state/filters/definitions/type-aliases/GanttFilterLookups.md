[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/filters/definitions](../index.md) / GanttFilterLookups

# Type Alias: GanttFilterLookups

> **GanttFilterLookups** = `object`

Defined in: [ui/src/components/gantt/state/filters/definitions.ts:15](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/gantt/state/filters/definitions.ts#L15)

Lookups the filter descriptions need to turn ids into names.

## Properties

### getCourse

> **getCourse**: (`id`) => [`Course`](../../../../../../api-shared/types/course/type-aliases/Course.md) \| `undefined`

Defined in: [ui/src/components/gantt/state/filters/definitions.ts:16](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/gantt/state/filters/definitions.ts#L16)

#### Parameters

##### id

[`CourseId`](../../../../../../api-shared/types/course/type-aliases/CourseId.md)

#### Returns

[`Course`](../../../../../../api-shared/types/course/type-aliases/Course.md) \| `undefined`

***

### getInstructor

> **getInstructor**: (`id`) => `CourseUser` \| `undefined`

Defined in: [ui/src/components/gantt/state/filters/definitions.ts:17](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/gantt/state/filters/definitions.ts#L17)

#### Parameters

##### id

`number`

#### Returns

`CourseUser` \| `undefined`
