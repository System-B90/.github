[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / prayerWindowsFromSettings

# Function: prayerWindowsFromSettings()

> **prayerWindowsFromSettings**(`settings`): `object`[]

Defined in: [ui/src/api-server/gantt/cut.ts:377](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/cut.ts#L377)

Prayer windows for the planner, read out of the MongoDB schedule settings.

The Gantt/Postgres side has no prayer data of its own, so the server is the
only layer that can bridge the two engines — the pure planner just receives
`"HH:mm"` strings. A malformed or missing setting simply contributes no
window: prayers are a soft preference and must never fail a cut.

## Parameters

### settings

[`PrayerSettings`](../../../../api-shared/types/settings/prayer/type-aliases/PrayerSettings.md) \| `null`

## Returns

`object`[]
