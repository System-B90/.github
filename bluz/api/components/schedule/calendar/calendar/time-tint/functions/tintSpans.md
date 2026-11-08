[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/time-tint](../index.md) / tintSpans

# Function: tintSpans()

> **tintSpans**(`shabbat`, `prayers`): [`TintSpan`](../type-aliases/TintSpan.md)[]

Defined in: [ui/src/components/schedule/calendar/calendar/time-tint.tsx:29](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/schedule/calendar/calendar/time-tint.tsx#L29)

The Shabbat window plus the prayer windows, prayers cut where they meet
Shabbat so the two translucent tints never stack.

## Parameters

### shabbat

[`PrayerSpan`](../../use-prayer-windows/type-aliases/PrayerSpan.md) \| `null`

### prayers

`Omit`\<[`TintSpan`](../type-aliases/TintSpan.md), `"kind"`\>[] \| `null`

## Returns

[`TintSpan`](../type-aliases/TintSpan.md)[]
