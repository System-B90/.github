[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/use-prayer-windows](../index.md) / usePrayerWindows

# Function: usePrayerWindows()

> **usePrayerWindows**(`date`, `enabled`, `iterationId?`): [`PrayerWindowSpan`](../type-aliases/PrayerWindowSpan.md)[] \| `null`

Defined in: [ui/src/components/schedule/calendar/calendar/use-prayer-windows.ts:51](https://github.com/System-B90/Bluz/blob/ef5f1592ad9f013b150ea581b494f4fff71a8490/ui/src/components/schedule/calendar/calendar/use-prayer-windows.ts#L51)

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
