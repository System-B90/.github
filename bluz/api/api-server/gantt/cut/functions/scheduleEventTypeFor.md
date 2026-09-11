[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / scheduleEventTypeFor

# Function: scheduleEventTypeFor()

> **scheduleEventTypeFor**(`ganttEvent`): [`EventType`](../../../../api-shared/types/event/enumerations/EventType.md)

Defined in: [ui/src/api-server/gantt/cut.ts:190](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/cut.ts#L190)

Calendar type of a cut occurrence. The auto-seeded meal events become real
break (הפסקה) events rather than generic "אחר" ones: the planner already
treats their windows as breaks while stacking, and once in the schedule they
must keep interrupting the events that split across breaks.

## Parameters

### ganttEvent

#### title

`string`

#### type

[`ModuleEventType`](../../../../api-shared/types/gantt/models/event/enumerations/ModuleEventType.md)

## Returns

[`EventType`](../../../../api-shared/types/event/enumerations/EventType.md)
