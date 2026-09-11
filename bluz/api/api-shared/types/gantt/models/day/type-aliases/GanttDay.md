[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/day](../index.md) / GanttDay

# Type Alias: GanttDay

> **GanttDay** = `object` & [`BaseGantItem`](../../shared/type-aliases/BaseGantItem.md)

Defined in: [ui/src/api-shared/types/gantt/models/day.ts:74](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/models/day.ts#L74)

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
