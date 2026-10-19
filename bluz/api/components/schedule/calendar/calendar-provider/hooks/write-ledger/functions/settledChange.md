[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/write-ledger](../index.md) / settledChange

# Function: settledChange()

> **settledChange**(`id`, `outcome`, `sent`): [`SettledChange`](../type-aliases/SettledChange.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/write-ledger.ts:115](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/calendar-provider/hooks/write-ledger.ts#L115)

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
