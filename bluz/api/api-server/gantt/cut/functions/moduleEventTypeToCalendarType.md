[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / moduleEventTypeToCalendarType

# Function: moduleEventTypeToCalendarType()

> **moduleEventTypeToCalendarType**(`type`): [`EventType`](../../../../api-shared/types/event/enumerations/EventType.md)

Defined in: [ui/src/api-server/gantt/cut.ts:177](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/gantt/cut.ts#L177)

Maps a Gantt module event type to its calendar counterpart. The enum values
are aligned one-to-one (הרצאה/ע"ע/ל"ע/אחר), but the mapping is explicit so a
future divergence is a compile error rather than a silent mismatch.

## Parameters

### type

[`ModuleEventType`](../../../../api-shared/types/gantt/models/event/enumerations/ModuleEventType.md)

## Returns

[`EventType`](../../../../api-shared/types/event/enumerations/EventType.md)
