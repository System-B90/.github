[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/server-clock](../index.md) / useAppDayRollover

# Function: useAppDayRollover()

> **useAppDayRollover**(`onRollover`, `__namedParameters?`): `void`

Defined in: [ui/src/components/base/server-clock.ts:133](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/server-clock.ts#L133)

Calls `onRollover(newDate, previousDate)` when the server's day (Jerusalem
time) changes: at midnight, on waking from sleep or returning to a tab whose
midnight timer never ran, and when a resync shows the day moved.

Runs only once the server clock is synced — before that there is no "today"
to roll over from. The timer only measures a duration; the hour is always
the server's.

## Parameters

### onRollover

(`date`, `previous`) => `void`

Receives the new and the previous `yyyy-MM-dd`.

### \_\_namedParameters?

#### enabled?

`boolean` = `true`

#### jitterMs?

`number` = `0`

## Returns

`void`
