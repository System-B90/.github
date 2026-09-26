[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-rules](../index.md) / BREAK\_PLACEMENT\_RULES

# Variable: BREAK\_PLACEMENT\_RULES

> `const` **BREAK\_PLACEMENT\_RULES**: `object`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:298](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-rules.ts#L298)

Structural rules that constrain *where* a break may go, independent of kind.

## Type Declaration

### adjacencyToleranceMinutes

> `readonly` **adjacencyToleranceMinutes**: `5` = `5`

Gap (minutes) under which a generated break counts as "directly
adjacent" to an existing break.

### earlierBreakGrowthCapMinutes

> `readonly` **earlierBreakGrowthCapMinutes**: `20` = `20`

Instead of a forbidden adjacent break, the pass grows an *earlier* break
in the same day, up to this many minutes. Keeps the recovered time in
the day without creating a second dead zone next to the meal.

### forbidAdjacentToExistingBreak

> `readonly` **forbidAdjacentToExistingBreak**: `true` = `true`

A generated break is never placed directly adjacent to an existing
הפסקה — a meal event or anything from the auto-seeded הפסקות syllabus.
Two touching breaks read as one long dead zone.

### implicitBreakCeilingMinutes

> `readonly` **implicitBreakCeilingMinutes**: `25` = `25`

Any single stretch of free time at or above this is an implicit break
the user never asked for. The pass redistributes rather than leaving it:
two well-placed breaks of 10 and 15 beat one of 25.

### minimumMaterializedMinutes

> `readonly` **minimumMaterializedMinutes**: `5` = `5`

Breaks shorter than this are not worth materializing as an event.

### redistributeTrailingSlack

> `readonly` **redistributeTrailingSlack**: `true` = `true`

Leftover slack is pushed into existing breaks (largest priority first)
before being left as trailing empty time at the end of the day.
