[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/write-ledger](../index.md) / SettledChange

# Type Alias: SettledChange

> **SettledChange** = \{ `id`: [`EventId`](../../../../../../../api-shared/types/event/type-aliases/EventId.md); `kind`: `"delete"`; \} \| \{ `event`: [`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md); `kind`: `"upsert"`; \}

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/write-ledger.ts:112](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/calendar/calendar-provider/hooks/write-ledger.ts#L112)

A settled write's effect on local state, if any.
