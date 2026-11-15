[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/SnapshotViewBanner](../index.md) / SnapshotViewBanner

# Function: SnapshotViewBanner()

> **SnapshotViewBanner**(`__namedParameters`): `Element` \| `null`

Defined in: [ui/src/components/schedule/calendar/calendar/SnapshotViewBanner.tsx:37](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/schedule/calendar/calendar/SnapshotViewBanner.tsx#L37)

Shown above the schedule while a snapshot is on show (`?snapshot=<id>`), so
it is never mistaken for the live schedule: what is on screen is read-only,
and the ways out — restore some of it, restore all of it, go back — are here.

## Parameters

### \_\_namedParameters

#### selectedEventIds

`ReadonlySet`\<`string`\>

The grid's multi-selection, the restore dialog's starting point.

## Returns

`Element` \| `null`
