[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/reload](../index.md) / ReloadConflict

# Type Alias: ReloadConflict

> **ReloadConflict** = `object`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:62](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/reload.ts#L62)

A gantt change blocked by a manual edit. `kind` mirrors what the reload would
have done: rewrite the event's fields, or archive it entirely.

## Properties

### changes

> **changes**: [`EventFieldChange`](../../../event-history/type-aliases/EventFieldChange.md)[]

Defined in: [ui/src/api-shared/types/gantt/reload.ts:69](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/reload.ts#L69)

Empty for `removal`.

***

### eventId

> **eventId**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:63](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/reload.ts#L63)

***

### ganttEventId

> **ganttEventId**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:64](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/reload.ts#L64)

***

### kind

> **kind**: `"removal"` \| `"update"`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:67](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/reload.ts#L67)

***

### lastManualEdit

> **lastManualEdit**: `null` \| [`ReloadConflictReason`](ReloadConflictReason.md)

Defined in: [ui/src/api-shared/types/gantt/reload.ts:71](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/reload.ts#L71)

Null when history exists but carries no attributable manual row.

***

### occurrenceDate

> **occurrenceDate**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:65](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/reload.ts#L65)

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:66](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/reload.ts#L66)
