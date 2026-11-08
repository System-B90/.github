[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/write-ledger](../index.md) / SettledChange

# Type Alias: SettledChange

> **SettledChange** = \{ `id`: [`EventId`](../../../../../../../api-shared/types/event/type-aliases/EventId.md); `kind`: `"delete"`; \} \| \{ `event`: [`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md); `kind`: `"upsert"`; \}

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/write-ledger.ts:112](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/hooks/write-ledger.ts#L112)

A settled write's effect on local state, if any.
