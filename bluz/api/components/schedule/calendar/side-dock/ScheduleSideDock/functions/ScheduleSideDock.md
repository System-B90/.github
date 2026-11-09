[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/side-dock/ScheduleSideDock](../index.md) / ScheduleSideDock

# Function: ScheduleSideDock()

> **ScheduleSideDock**(`__namedParameters`): `Element`

Defined in: [ui/src/components/schedule/calendar/side-dock/ScheduleSideDock.tsx:57](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/calendar/side-dock/ScheduleSideDock.tsx#L57)

The schedule's side dock: one narrow icon rail on the screen edge for the
unassigned-events box (ארגז) and the instructor list (מבוזרים), with a single
panel beside it. Users only ever work with one of the two at a time, so
opening one closes the other and the grid gives up at most one panel's
width. The rail itself takes a dragged tile to park it, so the box need not
be open to fill it.

## Parameters

### \_\_namedParameters

`ScheduleSideDockProps`

## Returns

`Element`
