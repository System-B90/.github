[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/calendar/utils](../index.md) / isWeekendInAppTimezone

# Function: isWeekendInAppTimezone()

> **isWeekendInAppTimezone**(`date`): `boolean`

Defined in: [ui/src/components/schedule/calendar/utils.ts:16](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/utils.ts#L16)

Whether a date falls on the weekend *in Israel time* (#613).

`Date.prototype.getDay()` answers in the browser's zone, so a viewer west of
Israel resolves a midnight-boundary column to the previous day and filters
the wrong columns out of the work week.

## Parameters

### date

`Date`

## Returns

`boolean`
