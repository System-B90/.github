[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/prayer-windows](../index.md) / DayPrayerWindow

# Type Alias: DayPrayerWindow

> **DayPrayerWindow** = `object`

Defined in: [ui/src/api-shared/types/prayer-windows.ts:12](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/prayer-windows.ts#L12)

When one daily prayer holds the students on one civil day, in Israel local
time (Beer Sheva). Drawn as a schedule tint, never stored as an event.

## Properties

### date

> **date**: `string`

Defined in: [ui/src/api-shared/types/prayer-windows.ts:14](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/prayer-windows.ts#L14)

Civil date, `YYYY-MM-DD`.

***

### end

> **end**: `string`

Defined in: [ui/src/api-shared/types/prayer-windows.ts:18](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/prayer-windows.ts#L18)

***

### prayer

> **prayer**: [`DailyPrayer`](DailyPrayer.md)

Defined in: [ui/src/api-shared/types/prayer-windows.ts:15](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/prayer-windows.ts#L15)

***

### reasons

> **reasons**: `string`[]

Defined in: [ui/src/api-shared/types/prayer-windows.ts:20](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/prayer-windows.ts#L20)

Hebrew names of what lengthens it (ראש חודש, קריאת התורה, …). Empty on a plain day.

***

### start

> **start**: `string`

Defined in: [ui/src/api-shared/types/prayer-windows.ts:17](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/prayer-windows.ts#L17)

Zero-padded `HH:mm`; `end` is `"24:00"` when the prayer runs past midnight.
