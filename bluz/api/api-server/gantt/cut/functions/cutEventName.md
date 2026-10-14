[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / cutEventName

# Function: cutEventName()

> **cutEventName**(`eventTitle`, `naming`, `eventSubjectId`, `symbolBySubjectId`): `string`

Defined in: [ui/src/api-server/gantt/cut.ts:333](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/gantt/cut.ts#L333)

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
