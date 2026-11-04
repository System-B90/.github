[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/hive-lesson-check](../index.md) / eventNeedsHiveLesson

# Function: eventNeedsHiveLesson()

> **eventNeedsHiveLesson**(`event`): `boolean`

Defined in: [ui/src/components/schedule/hive-lesson-check.ts:60](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/hive-lesson-check.ts#L60)

Whether an event should carry a Hive lesson at all: a subject-bound type
("אחר" only once a subject is set), real and visible to students.

## Parameters

### event

`Partial`\<`Pick`\<[`Event`](../../../../api-shared/types/event/type-aliases/Event.md), `"fake"` \| `"hidden"` \| `"subject"` \| `"type"`\>\>

The event to inspect.

## Returns

`boolean`

True when a missing lesson is worth flagging.
