[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/time-tint](../index.md) / TintSpan

# Type Alias: TintSpan

> **TintSpan** = [`PrayerSpan`](../../use-prayer-windows/type-aliases/PrayerSpan.md) & `object`

Defined in: [ui/src/components/schedule/calendar/calendar/time-tint.tsx:18](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/schedule/calendar/calendar/time-tint.tsx#L18)

A tinted stretch of time, epoch milliseconds, end exclusive. A prayer tint
keeps its whole window, uncut by Shabbat, for the tooltip.

## Type Declaration

### kind

> **kind**: [`TintKind`](TintKind.md)

### window?

> `optional` **window?**: [`DayPrayerWindow`](../../../../../../api-shared/types/prayer-windows/type-aliases/DayPrayerWindow.md)
