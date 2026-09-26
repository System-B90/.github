[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-breaks](../index.md) / PlacedItem

# Type Alias: PlacedItem

> **PlacedItem** = `object`

Defined in: [ui/src/api-shared/gantt/cut-breaks.ts:28](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-breaks.ts#L28)

One already-placed item on a day, in minutes-of-day.

## Properties

### endMinutes

> **endMinutes**: `number`

Defined in: [ui/src/api-shared/gantt/cut-breaks.ts:32](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-breaks.ts#L32)

***

### eventType

> **eventType**: [`ModuleEventType`](../../../types/gantt/models/event/enumerations/ModuleEventType.md)

Defined in: [ui/src/api-shared/gantt/cut-breaks.ts:33](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-breaks.ts#L33)

***

### isExistingBreak

> **isExistingBreak**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-breaks.ts:42](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-breaks.ts#L42)

True for meal events and anything from the הפסקות syllabus. No generated
break may sit directly against one of these.

***

### isPinned

> **isPinned**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-breaks.ts:44](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-breaks.ts#L44)

Pinned to a clock time (meals) — never shifted to make room for a break.

***

### key

> **key**: `string`

Defined in: [ui/src/api-shared/gantt/cut-breaks.ts:30](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-breaks.ts#L30)

Stable key matching the planner's slot key.

***

### roomName

> **roomName**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-breaks.ts:37](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-breaks.ts#L37)

Room name once the cut assigns rooms; null today.

***

### startMinutes

> **startMinutes**: `number`

Defined in: [ui/src/api-shared/gantt/cut-breaks.ts:31](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-breaks.ts#L31)

***

### syllabusId

> **syllabusId**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-breaks.ts:35](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-breaks.ts#L35)

Syllabus the event belongs to; drives the between-syllabuses rule.
