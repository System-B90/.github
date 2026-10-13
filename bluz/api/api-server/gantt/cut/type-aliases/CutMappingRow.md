[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / CutMappingRow

# Type Alias: CutMappingRow

> **CutMappingRow** = `object`

Defined in: [ui/src/api-server/gantt/cut.ts:97](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/gantt/cut.ts#L97)

Plain-data mapping row (subset of the Drizzle `cMDA` row).

## Properties

### allottedMinutes?

> `optional` **allottedMinutes?**: `null` \| `number`

Defined in: [ui/src/api-server/gantt/cut.ts:102](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/gantt/cut.ts#L102)

Minutes the event takes on this day.

***

### dayId

> **dayId**: `string`

Defined in: [ui/src/api-server/gantt/cut.ts:99](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/gantt/cut.ts#L99)

***

### eventId

> **eventId**: `null` \| `string`

Defined in: [ui/src/api-server/gantt/cut.ts:98](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/gantt/cut.ts#L98)

***

### sortOrder?

> `optional` **sortOrder?**: `null` \| `number`

Defined in: [ui/src/api-server/gantt/cut.ts:100](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/gantt/cut.ts#L100)

***

### weekOnly?

> `optional` **weekOnly?**: `boolean` \| `null`

Defined in: [ui/src/api-server/gantt/cut.ts:104](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/gantt/cut.ts#L104)

Placed for the week rather than this exact day (#964).
