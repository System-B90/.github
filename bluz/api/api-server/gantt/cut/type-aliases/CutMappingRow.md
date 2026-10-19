[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / CutMappingRow

# Type Alias: CutMappingRow

> **CutMappingRow** = `object`

Defined in: [ui/src/api-server/gantt/cut.ts:103](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/gantt/cut.ts#L103)

Plain-data mapping row (subset of the Drizzle `cMDA` row).

## Properties

### allottedMinutes?

> `optional` **allottedMinutes?**: `null` \| `number`

Defined in: [ui/src/api-server/gantt/cut.ts:108](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/gantt/cut.ts#L108)

Minutes the event takes on this day.

***

### dayId

> **dayId**: `string`

Defined in: [ui/src/api-server/gantt/cut.ts:105](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/gantt/cut.ts#L105)

***

### eventId

> **eventId**: `null` \| `string`

Defined in: [ui/src/api-server/gantt/cut.ts:104](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/gantt/cut.ts#L104)

***

### sortOrder?

> `optional` **sortOrder?**: `null` \| `number`

Defined in: [ui/src/api-server/gantt/cut.ts:106](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/gantt/cut.ts#L106)

***

### weekOnly?

> `optional` **weekOnly?**: `boolean` \| `null`

Defined in: [ui/src/api-server/gantt/cut.ts:110](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/gantt/cut.ts#L110)

Placed for the week rather than this exact day (#964).
