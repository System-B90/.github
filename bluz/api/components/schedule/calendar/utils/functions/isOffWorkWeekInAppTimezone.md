[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/calendar/utils](../index.md) / isOffWorkWeekInAppTimezone

# Function: isOffWorkWeekInAppTimezone()

> **isOffWorkWeekInAppTimezone**(`date`): `boolean`

Defined in: [ui/src/components/schedule/calendar/utils.ts:16](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/calendar/utils.ts#L16)

Whether a date falls outside the work week *in Israel time* (#613).

`Date.prototype.getDay()` answers in the browser's zone, so a viewer west of
Israel resolves a midnight-boundary column to the previous day and filters
the wrong columns out of the work week.

## Parameters

### date

`Date`

## Returns

`boolean`
