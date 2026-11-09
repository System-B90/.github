[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-dialog/gantt-link-candidates](../index.md) / ganttLinkCandidates

# Function: ganttLinkCandidates()

> **ganttLinkCandidates**(`curriculum`, `event`): [`GanttLinkCandidate`](../type-aliases/GanttLinkCandidate.md)[]

Defined in: [ui/src/components/schedule/event-dialog/gantt-link-candidates.ts:19](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/event-dialog/gantt-link-candidates.ts#L19)

Every event of the linked curriculum, in gantt order, scored against the
schedule event's Hive lesson (3), module (2) or subject (1) so the likely
match can be offered first.

## Parameters

### curriculum

`Pick`\<[`ApiCurriculum`](../../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md), `"c2s"`\>

### event

`Pick`\<`Partial`\<[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)\>, `"hiveLesson"` \| `"hiveModule"` \| `"subject"`\>

## Returns

[`GanttLinkCandidate`](../type-aliases/GanttLinkCandidate.md)[]
