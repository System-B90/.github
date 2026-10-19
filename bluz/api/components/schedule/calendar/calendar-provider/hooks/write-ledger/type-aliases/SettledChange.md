[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/write-ledger](../index.md) / SettledChange

# Type Alias: SettledChange

> **SettledChange** = \{ `id`: [`EventId`](../../../../../../../api-shared/types/event/type-aliases/EventId.md); `kind`: `"delete"`; \} \| \{ `event`: [`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md); `kind`: `"upsert"`; \}

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/write-ledger.ts:103](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/calendar-provider/hooks/write-ledger.ts#L103)

A settled write's effect on local state, if any.
