[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/time-tint](../index.md) / TintSpan

# Type Alias: TintSpan

> **TintSpan** = [`PrayerSpan`](../../use-prayer-windows/type-aliases/PrayerSpan.md) & `object`

Defined in: [ui/src/components/schedule/calendar/calendar/time-tint.tsx:18](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/calendar/calendar/time-tint.tsx#L18)

A tinted stretch of time, epoch milliseconds, end exclusive. A prayer tint
keeps its whole window, uncut by Shabbat, for the tooltip.

## Type Declaration

### kind

> **kind**: [`TintKind`](TintKind.md)

### window?

> `optional` **window?**: [`DayPrayerWindow`](../../../../../../api-shared/types/prayer-windows/type-aliases/DayPrayerWindow.md)
