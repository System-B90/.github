[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/day](../index.md) / GanttDay

# Type Alias: GanttDay

> **GanttDay** = `object` & [`BaseGantItem`](../../shared/type-aliases/BaseGantItem.md)

Defined in: [ui/src/api-shared/types/gantt/models/day.ts:75](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/gantt/models/day.ts#L75)

## Type Declaration

### comment?

> `optional` **comment?**: `string`

### dayEndTime?

> `optional` **dayEndTime?**: `null` \| `string`

End of this day's working window ("HH:mm"). The cut treats the span from
the day's start time to this as the day's capacity, and never places an
event past it. `null` ⇒ derive as start + GanttDay.totalWorkingMinutes,
which is how days behaved before the field existed.

### dayIndex

> **dayIndex**: [`GanttDayIndex`](../enumerations/GanttDayIndex.md)

### title

> `readonly` **title**: `string`

### totalWorkingMinutes

> **totalWorkingMinutes**: `number`

### weekId

> **weekId**: [`GanttWeekId`](../../week/type-aliases/GanttWeekId.md)
