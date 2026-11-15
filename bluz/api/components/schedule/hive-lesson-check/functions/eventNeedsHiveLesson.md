[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/hive-lesson-check](../index.md) / eventNeedsHiveLesson

# Function: eventNeedsHiveLesson()

> **eventNeedsHiveLesson**(`event`): `boolean`

Defined in: [ui/src/components/schedule/hive-lesson-check.ts:60](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/components/schedule/hive-lesson-check.ts#L60)

Whether an event should carry a Hive lesson at all: a subject-bound type
("אחר" only once a subject is set), real and visible to students.

## Parameters

### event

`Partial`\<`Pick`\<[`Event`](../../../../api-shared/types/event/type-aliases/Event.md), `"fake"` \| `"hidden"` \| `"subject"` \| `"type"`\>\>

The event to inspect.

## Returns

`boolean`

True when a missing lesson is worth flagging.
