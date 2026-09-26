[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/calendar/utils](../index.md) / getRangeForView

# Function: getRangeForView()

> **getRangeForView**(`newDate`, `view`): `DateRange`

Defined in: [ui/src/components/schedule/calendar/utils.ts:28](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/utils.ts#L28)

The instants a view spans, for range-scoped fetches and the ICS export.

Computed in Israel time rather than the browser's zone (#613): the grid's
columns are pinned there, so a range derived locally disagrees with what is
on screen for any viewer outside Israel — a Thursday-end computed in UTC is
already Friday in Jerusalem, which is exactly what #611 is about.

## Parameters

### newDate

`Date`

### view

`string`

## Returns

`DateRange`
