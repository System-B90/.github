[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/HiveLessonsProvider](../index.md) / HiveLessonsContextState

# Type Alias: HiveLessonsContextState

> **HiveLessonsContextState** = `object`

Defined in: [ui/src/components/base/HiveLessonsProvider.tsx:14](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/base/HiveLessonsProvider.tsx#L14)

## Properties

### default

> **default**: `boolean`

Defined in: [ui/src/components/base/HiveLessonsProvider.tsx:15](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/base/HiveLessonsProvider.tsx#L15)

***

### getLesson

> **getLesson**: (`id`) => [`HiveLesson`](../../../../api-shared/types/hive/type-aliases/HiveLesson.md) \| `undefined`

Defined in: [ui/src/components/base/HiveLessonsProvider.tsx:19](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/base/HiveLessonsProvider.tsx#L19)

#### Parameters

##### id

[`HiveLessonId`](../../../../api-shared/types/hive/type-aliases/HiveLessonId.md)

#### Returns

[`HiveLesson`](../../../../api-shared/types/hive/type-aliases/HiveLesson.md) \| `undefined`

***

### getLessonsOfModule

> **getLessonsOfModule**: (`moduleId`) => [`HiveLesson`](../../../../api-shared/types/hive/type-aliases/HiveLesson.md)[]

Defined in: [ui/src/components/base/HiveLessonsProvider.tsx:20](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/base/HiveLessonsProvider.tsx#L20)

#### Parameters

##### moduleId

`number`

#### Returns

[`HiveLesson`](../../../../api-shared/types/hive/type-aliases/HiveLesson.md)[]

***

### lessons

> **lessons**: [`HiveLesson`](../../../../api-shared/types/hive/type-aliases/HiveLesson.md)[]

Defined in: [ui/src/components/base/HiveLessonsProvider.tsx:16](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/base/HiveLessonsProvider.tsx#L16)

***

### loaded

> **loaded**: `boolean`

Defined in: [ui/src/components/base/HiveLessonsProvider.tsx:18](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/base/HiveLessonsProvider.tsx#L18)

True once Hive answered: until then a missing lesson is not news.
