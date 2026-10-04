[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-dialog/event-history](../index.md) / EventHistoryPanelProps

# Type Alias: EventHistoryPanelProps

> **EventHistoryPanelProps** = `object`

Defined in: [ui/src/components/schedule/event-dialog/event-history/index.tsx:39](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/schedule/event-dialog/event-history/index.tsx#L39)

"היסטוריית שינויים" — the audit trail of one schedule event, rendered inside
the event dialog. Collapsed by default (the dialog is an editing surface
first) and loaded lazily on first expand, so opening a dialog costs nothing
extra until the user asks for the history.

## Properties

### eventId

> **eventId**: [`EventId`](../../../../../api-shared/types/event/type-aliases/EventId.md)

Defined in: [ui/src/components/schedule/event-dialog/event-history/index.tsx:40](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/schedule/event-dialog/event-history/index.tsx#L40)
