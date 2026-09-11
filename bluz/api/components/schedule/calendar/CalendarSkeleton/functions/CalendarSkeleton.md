[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/calendar/CalendarSkeleton](../index.md) / CalendarSkeleton

# Function: CalendarSkeleton()

> **CalendarSkeleton**(): `Element`

Defined in: [ui/src/components/schedule/calendar/CalendarSkeleton.tsx:17](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/CalendarSkeleton.tsx#L17)

Stands in for the week grid while the first event fetch is in flight.
Rendered as an overlay rather than instead of the calendar: the calendar
itself is what reports the visible date range, and without it mounted no
fetch is ever issued.

Column order is irrelevant to RTL correctness here — the flex row inherits
the document's `dir="rtl"`, so it fills from the right like the real grid.

## Returns

`Element`
