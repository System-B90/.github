[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/hive-lesson-check](../index.md) / checkHiveLesson

# Function: checkHiveLesson()

> **checkHiveLesson**(`event`, `context`): [`HiveLessonIssue`](../type-aliases/HiveLessonIssue.md)[]

Defined in: [ui/src/components/schedule/hive-lesson-check.ts:76](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/hive-lesson-check.ts#L76)

Everything wrong with an event's Hive lesson, worst first; empty when the
lesson will reach every shuffle of the event.

## Parameters

### event

`Partial`\<`Pick`\<[`Event`](../../../../api-shared/types/event/type-aliases/Event.md), `"courses"` \| `"fake"` \| `"hidden"` \| `"hiveLesson"` \| `"hiveModule"` \| `"subject"` \| `"type"`\>\>

The event to check.

### context

[`HiveLessonCheckContext`](../type-aliases/HiveLessonCheckContext.md)

Hive lessons, Bluz courses and Hive groups.

## Returns

[`HiveLessonIssue`](../type-aliases/HiveLessonIssue.md)[]

The issues, each with a Hebrew message.
