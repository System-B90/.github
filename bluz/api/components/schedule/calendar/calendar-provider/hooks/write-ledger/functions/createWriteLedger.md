[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/write-ledger](../index.md) / createWriteLedger

# Function: createWriteLedger()

> **createWriteLedger**(): `object`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/write-ledger.ts:33](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/calendar-provider/hooks/write-ledger.ts#L33)

Orders optimistic event writes per event (#923). Each write claims a
sequence; a response only touches local state while its write is still the
newest for that event. A failed A→B after a successful B→C therefore no
longer restores A over C, and a late success no longer clobbers a newer
optimistic copy.

## Returns

### begin()

> **begin**(`id`, `before`): `number`

Claims a write.

#### Parameters

##### id

`string`

##### before

[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md) \| `null`

What the server holds if no write for `id` is in
       flight: the local copy being replaced, `null` for a creation.

#### Returns

`number`

### fail()

> **fail**(`id`, `seq`): [`WriteOutcome`](../type-aliases/WriteOutcome.md)

The server refused write `seq`: roll back only if it is the newest.

#### Parameters

##### id

`string`

##### seq

`number`

#### Returns

[`WriteOutcome`](../type-aliases/WriteOutcome.md)

### succeed()

> **succeed**(`id`, `seq`, `persisted`): [`WriteOutcome`](../type-aliases/WriteOutcome.md)

The server accepted write `seq`, which left it holding `persisted`.
Applied when it is the newest write, or when the newest one already
failed and rolled back — the server has moved on since.

#### Parameters

##### id

`string`

##### seq

`number`

##### persisted

[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md) \| `null`

#### Returns

[`WriteOutcome`](../type-aliases/WriteOutcome.md)
