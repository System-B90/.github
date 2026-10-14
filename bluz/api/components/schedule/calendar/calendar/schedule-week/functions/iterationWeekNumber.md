[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/schedule-week](../index.md) / iterationWeekNumber

# Function: iterationWeekNumber()

> **iterationWeekNumber**(`date`, `iterationStart`): `number` \| `null`

Defined in: [ui/src/components/schedule/calendar/calendar/schedule-week.ts:8](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/schedule/calendar/calendar/schedule-week.ts#L8)

The iteration week a calendar date falls in: week 1 is the Sunday-started
week containing the iteration's start date. Null before the iteration
starts or when there is no start date.

## Parameters

### date

`Date`

### iterationStart

`string` \| `Date` \| `null` \| `undefined`

## Returns

`number` \| `null`
