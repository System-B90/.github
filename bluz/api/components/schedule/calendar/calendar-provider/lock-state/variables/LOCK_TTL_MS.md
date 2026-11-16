[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar-provider/lock-state](../index.md) / LOCK\_TTL\_MS

# Variable: LOCK\_TTL\_MS

> `const` **LOCK\_TTL\_MS**: `30000` = `30_000`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/lock-state.ts:34](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/schedule/calendar/calendar-provider/lock-state.ts#L34)

How long a received lock survives without a refreshing heartbeat. Set to a
multiple of the heartbeat so a single dropped message never expires a lock
that is still genuinely held.
