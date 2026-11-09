[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/schedule-validation/common](../index.md) / activeEvents

# Function: activeEvents()

> **activeEvents**(`events`, `context`): [`Timed`](../type-aliases/Timed.md)[]

Defined in: [ui/src/api-shared/schedule-validation/common.ts:71](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/common.ts#L71)

The events a check sees: not hidden (unavailabilities and other hidden
markers never book a room or a person), not in the unassigned box, and
with a positive length. Sorted by start.

## Parameters

### events

readonly [`RuleCheckEvent`](../../types/type-aliases/RuleCheckEvent.md)[]

### context

[`RuleCheckContext`](../../types/type-aliases/RuleCheckContext.md)

## Returns

[`Timed`](../type-aliases/Timed.md)[]
