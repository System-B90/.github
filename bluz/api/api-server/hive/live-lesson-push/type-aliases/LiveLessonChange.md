[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/live-lesson-push](../index.md) / LiveLessonChange

# Type Alias: LiveLessonChange

> **LiveLessonChange** = `object`

Defined in: [ui/src/api-server/hive/live-lesson-push.ts:29](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/hive/live-lesson-push.ts#L29)

A saved edit of an event that was or is live.

## Properties

### after?

> `optional` **after?**: [`LiveLessonSide`](LiveLessonSide.md) & `object`

Defined in: [ui/src/api-server/hive/live-lesson-push.ts:34](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/hive/live-lesson-push.ts#L34)

The event as saved, when it is live.

#### Type Declaration

##### lessonId

> **lessonId**: [`HiveLessonId`](../../../../api-shared/types/hive/type-aliases/HiveLessonId.md)

***

### before?

> `optional` **before?**: [`LiveLessonSide`](LiveLessonSide.md)

Defined in: [ui/src/api-server/hive/live-lesson-push.ts:32](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/hive/live-lesson-push.ts#L32)

The event as it stood, when it was live.

***

### eventId

> **eventId**: [`EventId`](../../../../api-shared/types/event/type-aliases/EventId.md)

Defined in: [ui/src/api-server/hive/live-lesson-push.ts:30](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/hive/live-lesson-push.ts#L30)
