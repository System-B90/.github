[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/week-split](../index.md) / getWeekSplitDayIds

# Function: getWeekSplitDayIds()

> **getWeekSplitDayIds**(`startDayId`, `partCount`, `weeks`): `string`[]

Defined in: [ui/src/api-shared/gantt/week-split.ts:54](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/week-split.ts#L54)

The day each part runs on: the mapped day's position, repeated in each
following week (clamped to shorter weeks). Parts past the timeline's end are
dropped, so the result may be shorter than the split.

## Parameters

### startDayId

`string`

### partCount

`number`

### weeks

[`WeekSplitWeek`](../type-aliases/WeekSplitWeek.md)[]

## Returns

`string`[]
