[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/use-schedule-week](../index.md) / useScheduleWeek

# Function: useScheduleWeek()

> **useScheduleWeek**(`date`): `object`

Defined in: [ui/src/components/schedule/calendar/calendar/use-schedule-week.ts:13](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/calendar/calendar/use-schedule-week.ts#L13)

The iteration week shown in the calendar (counted from the viewed
iteration's start date) and the comment of the same-numbered week in the
gantt curriculum linked to that iteration, if any.

## Parameters

### date

`Date`

## Returns

`object`

### comment

> **comment**: `string`

### number

> **number**: `number` \| `null`

### weekStart

> **weekStart**: (`n`) => `Date` \| `null`

#### Parameters

##### n

`number`

#### Returns

`Date` \| `null`
