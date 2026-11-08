[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/SnapshotRestoreDialog](../index.md) / SnapshotRestoreDialog

# Function: SnapshotRestoreDialog()

> **SnapshotRestoreDialog**(`__namedParameters`): `Element`

Defined in: [ui/src/components/schedule/calendar/calendar/SnapshotRestoreDialog.tsx:61](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/schedule/calendar/calendar/SnapshotRestoreDialog.tsx#L61)

Picks which of a snapshot's differences to restore: every event the
snapshot and the live schedule disagree on, each with what a restore does
to it. Starts from the calendar's selection when it has one, else from all.

## Parameters

### \_\_namedParameters

#### iterationId

`string` \| `undefined`

#### onClose

() => `void`

#### onRestored

() => `void`

#### preselected

`ReadonlySet`\<`string`\>

The calendar's multi-selection; empty ⇒ everything starts checked.

#### view

[`SnapshotView`](../../../calendar-provider/CalendarContext/type-aliases/SnapshotView.md)

## Returns

`Element`
