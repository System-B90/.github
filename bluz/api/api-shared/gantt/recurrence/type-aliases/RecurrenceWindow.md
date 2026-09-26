[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/recurrence](../index.md) / RecurrenceWindow

# Type Alias: RecurrenceWindow

> **RecurrenceWindow** = `object`

Defined in: [ui/src/api-shared/gantt/recurrence.ts:14](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/recurrence.ts#L14)

Pure recurrence helpers for the Gantt timeline (#111).

A recurring event is placed on a single start day and then "echoes" forward
across the timeline: daily events repeat on every following day, weekly events
repeat on the same weekday of every following week. The recurrence is only
*satisfied* once an occurrence exists in every week of the curriculum — which,
given the forward echo, means the event must start in the very first week.
Until then an "unallocated" marker is shown in the first column.

## Properties

### dateOf?

> `optional` **dateOf?**: (`dayId`) => `string` \| `undefined`

Defined in: [ui/src/api-shared/gantt/recurrence.ts:20](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/recurrence.ts#L20)

Date of a timeline day ("YYYY-MM-DD"), or undefined when unknown.

#### Parameters

##### dayId

`string`

#### Returns

`string` \| `undefined`

***

### recurrenceEndDate?

> `optional` **recurrenceEndDate?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/recurrence.ts:18](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/recurrence.ts#L18)

Last date the recurrence may echo onto ("YYYY-MM-DD"), or null.

***

### recurrenceStartDate?

> `optional` **recurrenceStartDate?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/recurrence.ts:16](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/recurrence.ts#L16)

First date the recurrence may echo onto ("YYYY-MM-DD"), or null.
