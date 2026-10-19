[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/UseEventState](../index.md) / HistoryState

# Type Alias: HistoryState

> **HistoryState** = `object`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts:24](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts#L24)

Undo history as per-event inverse operations, not whole-array snapshots
(#935). A snapshot also captured every *other* user's state at that moment,
so undo reverted their live edits too - and pushed that to the server.

## Properties

### future

> **future**: `HistoryEntry`[]

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts:27](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts#L27)

***

### past

> **past**: `HistoryEntry`[]

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts:25](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts#L25)

***

### present

> **present**: [`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md)[]

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts:26](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts#L26)
