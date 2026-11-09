[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/use-prayer-windows](../index.md) / usePrayerWindows

# Function: usePrayerWindows()

> **usePrayerWindows**(`date`, `enabled`, `iterationId?`): [`PrayerWindowSpan`](../type-aliases/PrayerWindowSpan.md)[] \| `null`

Defined in: [ui/src/components/schedule/calendar/calendar/use-prayer-windows.ts:51](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/calendar/calendar/use-prayer-windows.ts#L51)

The server-computed prayer windows of the week holding `date`, in the viewed
iteration, or null while off, loading, or failed — the tint is a nicety.

## Parameters

### date

`Date`

### enabled

`boolean`

### iterationId?

`string`

## Returns

[`PrayerWindowSpan`](../type-aliases/PrayerWindowSpan.md)[] \| `null`
