[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/holidays](../index.md) / getHolidayComment

# Function: getHolidayComment()

> **getHolidayComment**(`date`): `string` \| `undefined`

Defined in: [ui/src/api-shared/gantt/holidays.ts:11](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/gantt/holidays.ts#L11)

Jewish holidays begin at sunset the evening before their civil (Gregorian)
date, so a holiday is "on" the day whose night carries it in. @hebcal/core
already resolves each holiday to that civil date, so no extra day-shift is
needed here - just look the date up.

## Parameters

### date

`Date`

## Returns

`string` \| `undefined`
