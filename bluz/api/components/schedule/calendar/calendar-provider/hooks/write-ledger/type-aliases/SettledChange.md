[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/write-ledger](../index.md) / SettledChange

# Type Alias: SettledChange

> **SettledChange** = \{ `id`: [`EventId`](../../../../../../../api-shared/types/event/type-aliases/EventId.md); `kind`: `"delete"`; \} \| \{ `event`: [`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md); `kind`: `"upsert"`; \}

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/write-ledger.ts:112](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/schedule/calendar/calendar-provider/hooks/write-ledger.ts#L112)

A settled write's effect on local state, if any.
