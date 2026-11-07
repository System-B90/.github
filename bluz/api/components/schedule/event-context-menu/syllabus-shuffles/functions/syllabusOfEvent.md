[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/syllabus-shuffles](../index.md) / syllabusOfEvent

# Function: syllabusOfEvent()

> **syllabusOfEvent**(`curriculum`, `event`): [`ApiSyllabus`](../../../../../api-shared/types/gantt/api-layer/type-aliases/ApiSyllabus.md) \| `null`

Defined in: [ui/src/components/schedule/event-context-menu/syllabus-shuffles.ts:11](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/schedule/event-context-menu/syllabus-shuffles.ts#L11)

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
