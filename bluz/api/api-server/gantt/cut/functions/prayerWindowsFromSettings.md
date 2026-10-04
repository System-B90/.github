[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / prayerWindowsFromSettings

# Function: prayerWindowsFromSettings()

> **prayerWindowsFromSettings**(`settings`): `object`[]

Defined in: [ui/src/api-server/gantt/cut.ts:313](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/gantt/cut.ts#L313)

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
