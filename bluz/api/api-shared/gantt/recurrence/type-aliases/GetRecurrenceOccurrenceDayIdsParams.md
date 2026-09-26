[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/recurrence](../index.md) / GetRecurrenceOccurrenceDayIdsParams

# Type Alias: GetRecurrenceOccurrenceDayIdsParams

> **GetRecurrenceOccurrenceDayIdsParams** = [`RecurrenceWindow`](RecurrenceWindow.md) & `object`

Defined in: [ui/src/api-shared/gantt/recurrence.ts:23](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/recurrence.ts#L23)

## Type Declaration

### allowedDayIndices?

> `optional` **allowedDayIndices?**: `null` \| `Set`\<[`GanttDayIndex`](../../../types/gantt/models/day/enumerations/GanttDayIndex.md)\>

Weekdays the event's temporal constraints permit it to land on, from
getAllowedDayIndices. `null`/undefined ⇒ unrestricted. An echo
whose weekday isn't in this set is skipped rather than forced (#111
follow-up): a recurring event only recurs on its valid days.

### dayIndexOf

> **dayIndexOf**: (`dayId`) => [`GanttDayIndex`](../../../types/gantt/models/day/enumerations/GanttDayIndex.md) \| `undefined`

Day-of-week for a day id, or undefined when unknown.

#### Parameters

##### dayId

`string`

#### Returns

[`GanttDayIndex`](../../../types/gantt/models/day/enumerations/GanttDayIndex.md) \| `undefined`

### excludedDayIds?

> `optional` **excludedDayIds?**: `Set`\<`string`\>

Occurrence days to skip — deleted or materialized into their own event.

### linearDays

> **linearDays**: `string`[]

Timeline day ids in chronological order.

### recurrence

> **recurrence**: [`EventRecurrence`](../../../types/gantt/models/event/enumerations/EventRecurrence.md)

### startDayId

> **startDayId**: `null` \| `string`

Day the event is mapped to, or null when unmapped.
