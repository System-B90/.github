[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-dialog/event-history](../index.md) / EventHistoryPanelProps

# Type Alias: EventHistoryPanelProps

> **EventHistoryPanelProps** = `object`

Defined in: [ui/src/components/schedule/event-dialog/event-history/index.tsx:39](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/event-dialog/event-history/index.tsx#L39)

"היסטוריית שינויים" — the audit trail of one schedule event, rendered inside
the event dialog. Collapsed by default (the dialog is an editing surface
first) and loaded lazily on first expand, so opening a dialog costs nothing
extra until the user asks for the history.

## Properties

### eventId

> **eventId**: [`EventId`](../../../../../api-shared/types/event/type-aliases/EventId.md)

Defined in: [ui/src/components/schedule/event-dialog/event-history/index.tsx:40](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/event-dialog/event-history/index.tsx#L40)
