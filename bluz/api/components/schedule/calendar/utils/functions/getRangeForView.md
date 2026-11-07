[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/calendar/utils](../index.md) / getRangeForView

# Function: getRangeForView()

> **getRangeForView**(`newDate`, `view`): `DateRange`

Defined in: [ui/src/components/schedule/calendar/utils.ts:29](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/schedule/calendar/utils.ts#L29)

The instants a view spans, for range-scoped fetches and the ICS export.

Computed in Israel time rather than the browser's zone (#613): the grid's
columns are pinned there, so a range derived locally disagrees with what is
on screen for any viewer outside Israel — a Friday-end computed in UTC is
already Saturday in Jerusalem, which is exactly what #611 is about.

## Parameters

### newDate

`Date`

### view

`string`

## Returns

`DateRange`
