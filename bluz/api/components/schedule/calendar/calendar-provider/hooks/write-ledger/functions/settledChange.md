[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/write-ledger](../index.md) / settledChange

# Function: settledChange()

> **settledChange**(`id`, `outcome`, `sent`): [`SettledChange`](../type-aliases/SettledChange.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/write-ledger.ts:124](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/calendar/calendar-provider/hooks/write-ledger.ts#L124)

Turns a write outcome into the local-state change it calls for. A
confirmation only re-applies a real server-side normalization (#156); a
rollback is stamped just past the write it undoes, so a newer broadcast from
another client still wins over it in isStaleUpsert.

## Parameters

### id

`string`

### outcome

[`WriteOutcome`](../type-aliases/WriteOutcome.md)

### sent

[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md) \| `null`

What the settled write sent; `null` for a delete.

## Returns

[`SettledChange`](../type-aliases/SettledChange.md) \| `null`
