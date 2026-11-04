[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / CutMappingRow

# Type Alias: CutMappingRow

> **CutMappingRow** = `object`

Defined in: [ui/src/api-server/gantt/cut.ts:112](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/gantt/cut.ts#L112)

Plain-data mapping row (subset of the Drizzle `cMDA` row).

## Properties

### allottedMinutes?

> `optional` **allottedMinutes?**: `null` \| `number`

Defined in: [ui/src/api-server/gantt/cut.ts:117](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/gantt/cut.ts#L117)

Minutes the event takes on this day.

***

### dayId

> **dayId**: `string`

Defined in: [ui/src/api-server/gantt/cut.ts:114](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/gantt/cut.ts#L114)

***

### eventId

> **eventId**: `null` \| `string`

Defined in: [ui/src/api-server/gantt/cut.ts:113](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/gantt/cut.ts#L113)

***

### sortOrder?

> `optional` **sortOrder?**: `null` \| `number`

Defined in: [ui/src/api-server/gantt/cut.ts:115](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/gantt/cut.ts#L115)

***

### weekOnly?

> `optional` **weekOnly?**: `boolean` \| `null`

Defined in: [ui/src/api-server/gantt/cut.ts:119](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/gantt/cut.ts#L119)

Placed for the week rather than this exact day (#964).
