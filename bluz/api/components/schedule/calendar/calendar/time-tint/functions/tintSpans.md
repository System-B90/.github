[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/time-tint](../index.md) / tintSpans

# Function: tintSpans()

> **tintSpans**(`shabbat`, `prayers`): [`TintSpan`](../type-aliases/TintSpan.md)[]

Defined in: [ui/src/components/schedule/calendar/calendar/time-tint.tsx:30](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/schedule/calendar/calendar/time-tint.tsx#L30)

The Shabbat window plus the prayer windows, prayers cut where they meet
Shabbat so the two translucent tints never stack.

## Parameters

### shabbat

[`PrayerSpan`](../../use-prayer-windows/type-aliases/PrayerSpan.md) \| `null`

### prayers

`Omit`\<[`TintSpan`](../type-aliases/TintSpan.md), `"kind"`\>[] \| `null`

## Returns

[`TintSpan`](../type-aliases/TintSpan.md)[]
