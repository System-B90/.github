[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/schedule-feed](../index.md) / HiveFeedLookup

# Type Alias: HiveFeedLookup

> **HiveFeedLookup** = `object`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:90](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/hive/schedule-feed.ts#L90)

Hive names the feed resolves Bluz ids against.

## Properties

### groupEmails

> **groupEmails**: (`courseIds`) => `string`[]

Defined in: [ui/src/api-server/hive/schedule-feed.ts:97](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/hive/schedule-feed.ts#L97)

Group emails of the courses and all their sub-courses, deduplicated.

#### Parameters

##### courseIds

[`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)[]

#### Returns

`string`[]

***

### lesson

> **lesson**: (`lessonId`) => \{ `name`: `string`; `subjectName`: `string`; \} \| `undefined`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:92](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/hive/schedule-feed.ts#L92)

#### Parameters

##### lessonId

[`HiveLessonId`](../../../../api-shared/types/hive/type-aliases/HiveLessonId.md)

#### Returns

\{ `name`: `string`; `subjectName`: `string`; \} \| `undefined`

***

### roomName

> **roomName**: (`roomId`) => `string` \| `undefined`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:95](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/hive/schedule-feed.ts#L95)

#### Parameters

##### roomId

`number`

#### Returns

`string` \| `undefined`

***

### subjectName

> **subjectName**: (`subjectId`) => `string` \| `undefined`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:91](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/hive/schedule-feed.ts#L91)

#### Parameters

##### subjectId

`number`

#### Returns

`string` \| `undefined`
