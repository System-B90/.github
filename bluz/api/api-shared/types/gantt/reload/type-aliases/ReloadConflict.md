[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/reload](../index.md) / ReloadConflict

# Type Alias: ReloadConflict

> **ReloadConflict** = `object`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:57](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/reload.ts#L57)

A gantt change blocked by a manual edit. `kind` mirrors what the reload would
have done: rewrite the event's fields, or archive it entirely.

## Properties

### changes

> **changes**: [`EventFieldChange`](../../../event-history/type-aliases/EventFieldChange.md)[]

Defined in: [ui/src/api-shared/types/gantt/reload.ts:64](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/reload.ts#L64)

Empty for `removal`.

***

### eventId

> **eventId**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:58](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/reload.ts#L58)

***

### ganttEventId

> **ganttEventId**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:59](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/reload.ts#L59)

***

### kind

> **kind**: `"removal"` \| `"update"`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:62](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/reload.ts#L62)

***

### lastManualEdit

> **lastManualEdit**: `null` \| [`ReloadConflictReason`](ReloadConflictReason.md)

Defined in: [ui/src/api-shared/types/gantt/reload.ts:66](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/reload.ts#L66)

Null when history exists but carries no attributable manual row.

***

### occurrenceDate

> **occurrenceDate**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:60](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/reload.ts#L60)

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:61](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/reload.ts#L61)
