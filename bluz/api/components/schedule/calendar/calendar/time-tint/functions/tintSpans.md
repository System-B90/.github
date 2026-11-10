[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/time-tint](../index.md) / tintSpans

# Function: tintSpans()

> **tintSpans**(`shabbat`, `prayers`): [`TintSpan`](../type-aliases/TintSpan.md)[]

Defined in: [ui/src/components/schedule/calendar/calendar/time-tint.tsx:30](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/schedule/calendar/calendar/time-tint.tsx#L30)

The Shabbat window plus the prayer windows, prayers cut where they meet
Shabbat so the two translucent tints never stack.

## Parameters

### shabbat

[`PrayerSpan`](../../use-prayer-windows/type-aliases/PrayerSpan.md) \| `null`

### prayers

`Omit`\<[`TintSpan`](../type-aliases/TintSpan.md), `"kind"`\>[] \| `null`

## Returns

[`TintSpan`](../type-aliases/TintSpan.md)[]
