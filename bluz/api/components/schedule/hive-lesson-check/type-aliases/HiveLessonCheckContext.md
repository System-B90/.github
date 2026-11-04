[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/hive-lesson-check](../index.md) / HiveLessonCheckContext

# Type Alias: HiveLessonCheckContext

> **HiveLessonCheckContext** = `object`

Defined in: [ui/src/components/schedule/hive-lesson-check.ts:26](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/hive-lesson-check.ts#L26)

## Properties

### getLesson?

> `optional` **getLesson?**: (`id`) => [`HiveLesson`](../../../../api-shared/types/hive/type-aliases/HiveLesson.md) \| `undefined`

Defined in: [ui/src/components/schedule/hive-lesson-check.ts:28](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/hive-lesson-check.ts#L28)

Hive's lessons; undefined while they load, so nothing is claimed missing.

#### Parameters

##### id

[`HiveLessonId`](../../../../api-shared/types/hive/type-aliases/HiveLessonId.md)

#### Returns

[`HiveLesson`](../../../../api-shared/types/hive/type-aliases/HiveLesson.md) \| `undefined`

***

### unmatchedCourses?

> `optional` **unmatchedCourses?**: (`courseIds`) => `string`[]

Defined in: [ui/src/components/schedule/hive-lesson-check.ts:33](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/hive-lesson-check.ts#L33)

The given courses that reach no Hive group, by name; undefined while
Hive's groups load or are unreachable. See [unmatchedCoursesResolver](../functions/unmatchedCoursesResolver.md).

#### Parameters

##### courseIds

`string`[]

#### Returns

`string`[]
