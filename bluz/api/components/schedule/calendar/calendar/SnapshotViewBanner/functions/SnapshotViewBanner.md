[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/SnapshotViewBanner](../index.md) / SnapshotViewBanner

# Function: SnapshotViewBanner()

> **SnapshotViewBanner**(`__namedParameters`): `Element` \| `null`

Defined in: [ui/src/components/schedule/calendar/calendar/SnapshotViewBanner.tsx:37](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/schedule/calendar/calendar/SnapshotViewBanner.tsx#L37)

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
