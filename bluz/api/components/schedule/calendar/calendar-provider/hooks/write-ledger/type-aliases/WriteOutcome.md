[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/write-ledger](../index.md) / WriteOutcome

# Type Alias: WriteOutcome

> **WriteOutcome** = \{ `event`: [`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md) \| `null`; `kind`: `"apply"`; \} \| \{ `event`: [`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md) \| `null`; `kind`: `"confirm"`; \} \| \{ `kind`: `"ignore"`; \}

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/write-ledger.ts:5](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/schedule/calendar/calendar-provider/hooks/write-ledger.ts#L5)

What a settled write should do to local state.

## Union Members

### Type Literal

\{ `event`: [`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md) \| `null`; `kind`: `"apply"`; \}

Show this server state (`null`: the event is not on the server).

***

### Type Literal

\{ `event`: [`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md) \| `null`; `kind`: `"confirm"`; \}

The newest write was accepted; `event` is what the server echoed.

***

### Type Literal

\{ `kind`: `"ignore"`; \}

Leave local state alone: a newer write owns this event now.
