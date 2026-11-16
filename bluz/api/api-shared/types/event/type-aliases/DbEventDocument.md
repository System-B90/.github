[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / DbEventDocument

# Type Alias: DbEventDocument

> **DbEventDocument** = `Omit`\<[`Event`](Event.md), `"endTime"` \| `"startTime"`\> & `object`

Defined in: [ui/src/api-shared/types/event.ts:342](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/api-shared/types/event.ts#L342)

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
