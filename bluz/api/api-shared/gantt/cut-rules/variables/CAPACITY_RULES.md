[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-rules](../index.md) / CAPACITY\_RULES

# Variable: CAPACITY\_RULES

> `const` **CAPACITY\_RULES**: `object`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:32](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-rules.ts#L32)

A day's capacity is its **working window**: the clock span from the day's
start time to its end time (`GanttDay.dayEndTime`). Not a minute budget — a
wall-clock range, so a pinned meal at 13:00 anchors real time rather than
merely consuming a quota.

Everything placed inside the window counts against it: lessons, pinned meal
events, and generated הפסקה breaks alike.

## Type Declaration

### fallbackDayEndTime

> `readonly` **fallbackDayEndTime**: `"21:00"` = `"21:00"`

Fallback end time for a day with no explicit `dayEndTime` — used only
when a row predates the column and the migration backfill has not run.
Days at capacity 0 (typically שבת) are never spill targets regardless.

### negligibleSlackMinutes

> `readonly` **negligibleSlackMinutes**: `5` = `5`

Slack under this many minutes is treated as zero. Prevents the balancer
from shuffling an event across days to reclaim a trivial remainder.
