[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCurriculumCutPayload

# Type Alias: ApiCurriculumCutPayload

> **ApiCurriculumCutPayload** = `object`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:17](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L17)

API contract for the curriculum → schedule cut ("גזירה ללו"ז", #118).
The endpoint materializes a published curriculum's gantt data into schedule
events in the linked iteration's MongoDB. All inputs are derived server-side
from the curriculum id, so the request carries no payload.

## Properties

### acceptedConstraintMoves?

> `optional` **acceptedConstraintMoves?**: `string`[]

Defined in: [ui/src/api-shared/types/gantt/cut.ts:43](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L43)

Event ids whose constraint-solver moves the user accepted in the dialog.
Anything not listed is reported but never moved.

***

### autoSpillover?

> `optional` **autoSpillover?**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:28](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L28)

Rebalance each week so no day exceeds its working window, cascading work
forward within the week. Defaults to on.

***

### force?

> `optional` **force?**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:23](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L23)

Cut anyway despite unmapped events / unsatisfied recurrences (an
unfinished gantt). The user explicitly acknowledges the gap; those
events are dropped from the cut instead of blocking it.

***

### insertBreaks?

> `optional` **insertBreaks?**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:33](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L33)

Spread each day's leftover slack through the day as real הפסקה events
instead of leaving it as an empty tail. Defaults to on.

***

### parkWeekOnly?

> `optional` **parkWeekOnly?**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:38](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L38)

Put week-only mappings in the schedule's unassigned box (ארגז) instead
of auto-scheduling them. Defaults to off.

***

### templateId?

> `optional` **templateId?**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:58](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L58)

Week template to cut with (#997): its events' placements and its day
start, meal and prayer times. Omitted ⇒ the default template.

***

### weekId?

> `optional` **weekId?**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:53](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L53)

Cut only this timeline week (#970). Its earlier cut events are replaced;
every other week is left as it is. Omitted ⇒ the whole curriculum.

***

### weekOverflowResolutions?

> `optional` **weekOverflowResolutions?**: `Record`\<`string`, [`WeekOverflowResolution`](../../../../gantt/cut-rules/type-aliases/WeekOverflowResolution.md)\>

Defined in: [ui/src/api-shared/types/gantt/cut.ts:48](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L48)

The user's answer to each `week-overflow` decision, keyed by week id.
Weeks left out fall back to `OVERFLOW_RULES.defaultResolution`.
