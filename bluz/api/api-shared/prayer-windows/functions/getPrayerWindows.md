[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/prayer-windows](../index.md) / getPrayerWindows

# Function: getPrayerWindows()

> **getPrayerWindows**(`date`, `times`): [`DayPrayerWindow`](../../types/prayer-windows/type-aliases/DayPrayerWindow.md)[]

Defined in: [ui/src/api-shared/prayer-windows.ts:204](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/prayer-windows.ts#L204)

The daily prayer windows of the Sunday-to-Saturday week holding `date`, at
`times`. Each lasts its plain-weekday length (BASE\_MINUTES) plus
what its day adds (ADDED\_MINUTES). None falls in Shabbat or a Yom Tov, and the evening
one begins has no weekday ערבית: those prayers are not the weekday ones, and
nothing is scheduled then anyway. Pure, like `getShabbatWindow`.

## Parameters

### date

`string`

### times

[`PrayerTimes`](../type-aliases/PrayerTimes.md)

## Returns

[`DayPrayerWindow`](../../types/prayer-windows/type-aliases/DayPrayerWindow.md)[]
