[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCurriculumCutPayload

# Type Alias: ApiCurriculumCutPayload

> **ApiCurriculumCutPayload** = `object`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:17](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/cut.ts#L17)

API contract for the curriculum → schedule cut ("גזירה ללו"ז", #118).
The endpoint materializes a published curriculum's gantt data into schedule
events in the linked iteration's MongoDB. All inputs are derived server-side
from the curriculum id, so the request carries no payload.

## Properties

### acceptedConstraintMoves?

> `optional` **acceptedConstraintMoves?**: `string`[]

Defined in: [ui/src/api-shared/types/gantt/cut.ts:38](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/cut.ts#L38)

Event ids whose constraint-solver moves the user accepted in the dialog.
Anything not listed is reported but never moved.

***

### autoSpillover?

> `optional` **autoSpillover?**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:28](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/cut.ts#L28)

Rebalance each week so no day exceeds its working window, cascading work
forward within the week. Defaults to on.

***

### force?

> `optional` **force?**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:23](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/cut.ts#L23)

Cut anyway despite unmapped events / unsatisfied recurrences (an
unfinished gantt). The user explicitly acknowledges the gap; those
events are dropped from the cut instead of blocking it.

***

### insertBreaks?

> `optional` **insertBreaks?**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:33](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/cut.ts#L33)

Spread each day's leftover slack through the day as real הפסקה events
instead of leaving it as an empty tail. Defaults to on.

***

### weekOverflowResolutions?

> `optional` **weekOverflowResolutions?**: `Record`\<`string`, [`WeekOverflowResolution`](../../../../gantt/cut-rules/type-aliases/WeekOverflowResolution.md)\>

Defined in: [ui/src/api-shared/types/gantt/cut.ts:43](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/cut.ts#L43)

The user's answer to each `week-overflow` decision, keyed by week id.
Weeks left out fall back to `OVERFLOW_RULES.defaultResolution`.
