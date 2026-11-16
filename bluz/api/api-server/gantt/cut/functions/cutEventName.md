[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / cutEventName

# Function: cutEventName()

> **cutEventName**(`eventTitle`, `naming`, `eventSubjectId`, `symbolBySubjectId`): `string`

Defined in: [ui/src/api-server/gantt/cut.ts:353](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-server/gantt/cut.ts#L353)

`{syllabus} - {gantt_event_name}` (#965). `{syllabus}` is the syllabus's own
short name (#973), else its Hive subject's symbol — the syllabus link first,
then the event's resolved subject — else the syllabus title.

## Parameters

### eventTitle

`string`

### naming

[`SyllabusNaming`](../type-aliases/SyllabusNaming.md) \| `undefined`

### eventSubjectId

`number` \| `null`

### symbolBySubjectId

`Map`\<`number`, `string`\>

## Returns

`string`
