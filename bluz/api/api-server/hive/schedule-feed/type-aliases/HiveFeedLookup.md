[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/schedule-feed](../index.md) / HiveFeedLookup

# Type Alias: HiveFeedLookup

> **HiveFeedLookup** = `object`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:55](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/hive/schedule-feed.ts#L55)

Hive names the feed resolves Bluz ids against.

## Properties

### groupEmail

> **groupEmail**: (`courseId`) => `string` \| `undefined`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:61](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/hive/schedule-feed.ts#L61)

#### Parameters

##### courseId

[`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)

#### Returns

`string` \| `undefined`

***

### lesson

> **lesson**: (`lessonId`) => \{ `name`: `string`; `subjectName`: `string`; \} \| `undefined`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:57](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/hive/schedule-feed.ts#L57)

#### Parameters

##### lessonId

[`HiveLessonId`](../../../../api-shared/types/hive/type-aliases/HiveLessonId.md)

#### Returns

\{ `name`: `string`; `subjectName`: `string`; \} \| `undefined`

***

### roomName

> **roomName**: (`roomId`) => `string` \| `undefined`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:60](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/hive/schedule-feed.ts#L60)

#### Parameters

##### roomId

`number`

#### Returns

`string` \| `undefined`

***

### subjectName

> **subjectName**: (`subjectId`) => `string` \| `undefined`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:56](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/hive/schedule-feed.ts#L56)

#### Parameters

##### subjectId

`number`

#### Returns

`string` \| `undefined`
