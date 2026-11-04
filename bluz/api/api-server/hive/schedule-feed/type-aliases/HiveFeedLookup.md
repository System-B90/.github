[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/schedule-feed](../index.md) / HiveFeedLookup

# Type Alias: HiveFeedLookup

> **HiveFeedLookup** = `object`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:112](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/hive/schedule-feed.ts#L112)

Hive names the feed resolves Bluz ids against.

## Properties

### category

> **category**: (`eventType`) => [`HiveFeedCategory`](HiveFeedCategory.md) \| `undefined`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:121](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/hive/schedule-feed.ts#L121)

The Hive category matching a Bluz event type, if Hive has one.

#### Parameters

##### eventType

`string`

#### Returns

[`HiveFeedCategory`](HiveFeedCategory.md) \| `undefined`

***

### dailyReviewLesson

> **dailyReviewLesson**: (`moduleId`) => `HiveFeedLesson` \| `undefined`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:119](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/hive/schedule-feed.ts#L119)

The lesson of Hive's daily-review module, when `moduleId` is that
module; undefined for every other module.

#### Parameters

##### moduleId

`number`

#### Returns

`HiveFeedLesson` \| `undefined`

***

### groupEmails

> **groupEmails**: (`courseIds`) => `string`[]

Defined in: [ui/src/api-server/hive/schedule-feed.ts:124](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/hive/schedule-feed.ts#L124)

Group emails of the courses and all their sub-courses, deduplicated.

#### Parameters

##### courseIds

[`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)[]

#### Returns

`string`[]

***

### lesson

> **lesson**: (`lessonId`) => `HiveFeedLesson` \| `undefined`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:114](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/hive/schedule-feed.ts#L114)

#### Parameters

##### lessonId

[`HiveLessonId`](../../../../api-shared/types/hive/type-aliases/HiveLessonId.md)

#### Returns

`HiveFeedLesson` \| `undefined`

***

### roomName

> **roomName**: (`roomId`) => `string` \| `undefined`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:122](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/hive/schedule-feed.ts#L122)

#### Parameters

##### roomId

`number`

#### Returns

`string` \| `undefined`

***

### subjectName

> **subjectName**: (`subjectId`) => `string` \| `undefined`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:113](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/hive/schedule-feed.ts#L113)

#### Parameters

##### subjectId

`number`

#### Returns

`string` \| `undefined`
