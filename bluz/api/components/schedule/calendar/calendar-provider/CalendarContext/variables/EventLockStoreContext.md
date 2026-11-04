[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar-provider/CalendarContext](../index.md) / EventLockStoreContext

# Variable: EventLockStoreContext

> `const` **EventLockStoreContext**: `Context`\<[`EventLockStore`](../type-aliases/EventLockStore.md)\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:88](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L88)

The live lock map as a store with one stable identity (#955). Tiles read
their own lock through [useEventLock](../functions/useEventLock.md) instead of `useCalendar()`,
which re-rendered every tile on every event change and every lock change.
Outside a provider it is an empty store, so a tile renders in isolation.
