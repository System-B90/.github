[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar-provider/CalendarContext](../index.md) / EventLockStoreContext

# Variable: EventLockStoreContext

> `const` **EventLockStoreContext**: `Context`\<[`EventLockStore`](../type-aliases/EventLockStore.md)\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:82](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L82)

The live lock map as a store with one stable identity (#955). Tiles read
their own lock through [useEventLock](../functions/useEventLock.md) instead of `useCalendar()`,
which re-rendered every tile on every event change and every lock change.
Outside a provider it is an empty store, so a tile renders in isolation.
