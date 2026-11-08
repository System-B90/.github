[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / cutEventName

# Function: cutEventName()

> **cutEventName**(`eventTitle`, `naming`, `eventSubjectId`, `symbolBySubjectId`): `string`

Defined in: [ui/src/api-server/gantt/cut.ts:353](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/gantt/cut.ts#L353)

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
