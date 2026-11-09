[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/syllabus-shuffles](../index.md) / syllabusOfEvent

# Function: syllabusOfEvent()

> **syllabusOfEvent**(`curriculum`, `event`): [`ApiSyllabus`](../../../../../api-shared/types/gantt/api-layer/type-aliases/ApiSyllabus.md) \| `null`

Defined in: [ui/src/components/schedule/event-context-menu/syllabus-shuffles.ts:11](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/event-context-menu/syllabus-shuffles.ts#L11)

The gantt syllabus an event was cut from: the one owning its gantt event,
else the only syllabus carrying its Hive subject. Null when neither is
conclusive.

## Parameters

### curriculum

`Pick`\<[`ApiCurriculum`](../../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md), `"c2s"`\>

### event

`Pick`\<[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md), `"ganttEventId"` \| `"subject"`\>

## Returns

[`ApiSyllabus`](../../../../../api-shared/types/gantt/api-layer/type-aliases/ApiSyllabus.md) \| `null`
