[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-rules](../index.md) / PRAYER\_RULES

# Variable: PRAYER\_RULES

> `const` **PRAYER\_RULES**: `object`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:350](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-rules.ts#L350)

Prayers (שחרית / מנחה / ערבית) come from the schedule settings in MongoDB and
are handed to the pure planner by `api-server/gantt/cut.ts`.

They are **soft** windows, unlike meals:
- The break pass prefers to position a break so it covers a prayer.
- A lecture that lands on a prayer is re-ordered within its day when that is
  possible without pushing the day past its end time — otherwise it simply
  overlaps. A prayer never forces spillover and never extends a day.

## Type Declaration

### avoidOverlapForTypes

> `readonly` **avoidOverlapForTypes**: readonly [`ModuleEventType`](../../../types/gantt/models/event/enumerations/ModuleEventType.md)[]

Event types that should not sit on top of a prayer, best-effort.

### coverageThresholdMinutes

> `readonly` **coverageThresholdMinutes**: `10` = `10`

A break counts as "covering" a prayer when it overlaps the prayer window
by at least this many minutes.

### defaultDurationMinutes

> `readonly` **defaultDurationMinutes**: `20` = `20`

Assumed length of a prayer window when settings carry only a start time.

### mayExtendDay

> `readonly` **mayExtendDay**: `false` = `false`

Prayers are never allowed to push the day past its end time.
