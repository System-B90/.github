[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / DbEventDocument

# Type Alias: DbEventDocument

> **DbEventDocument** = `Omit`\<[`Event`](Event.md), `"endTime"` \| `"startTime"`\> & `object`

Defined in: [ui/src/api-shared/types/event.ts:317](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/event.ts#L317)

## Type Declaration

### archived?

> `optional` **archived?**: `boolean`

Soft-delete marker. When `true` the event has been archived (deleted by
the user) and must be excluded from all active views. Absent/`false`
means the event is live.

### endTime

> **endTime**: `Date`

### startTime

> **startTime**: `Date`
