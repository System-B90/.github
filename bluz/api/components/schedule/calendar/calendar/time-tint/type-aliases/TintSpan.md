[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/time-tint](../index.md) / TintSpan

# Type Alias: TintSpan

> **TintSpan** = [`PrayerSpan`](../../use-prayer-windows/type-aliases/PrayerSpan.md) & `object`

Defined in: [ui/src/components/schedule/calendar/calendar/time-tint.tsx:19](https://github.com/System-B90/Bluz/blob/ef5f1592ad9f013b150ea581b494f4fff71a8490/ui/src/components/schedule/calendar/calendar/time-tint.tsx#L19)

A tinted stretch of time, epoch milliseconds, end exclusive. A prayer tint
keeps its whole window, uncut by Shabbat, for the tooltip.

## Type Declaration

### kind

> **kind**: [`TintKind`](TintKind.md)

### window?

> `optional` **window?**: [`DayPrayerWindow`](../../../../../../api-shared/types/prayer-windows/type-aliases/DayPrayerWindow.md)
