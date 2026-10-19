[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / moduleEventTypeToCalendarType

# Function: moduleEventTypeToCalendarType()

> **moduleEventTypeToCalendarType**(`type`): [`EventType`](../../../../api-shared/types/event/enumerations/EventType.md)

Defined in: [ui/src/api-server/gantt/cut.ts:187](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/cut.ts#L187)

Maps a Gantt module event type to its calendar counterpart. The enum values
are aligned one-to-one (הרצאה/ע"ע/ל"ע/אחר), but the mapping is explicit so a
future divergence is a compile error rather than a silent mismatch.

## Parameters

### type

[`ModuleEventType`](../../../../api-shared/types/gantt/models/event/enumerations/ModuleEventType.md)

## Returns

[`EventType`](../../../../api-shared/types/event/enumerations/EventType.md)
