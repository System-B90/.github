[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / CutMappingRow

# Type Alias: CutMappingRow

> **CutMappingRow** = `object`

Defined in: [ui/src/api-server/gantt/cut.ts:95](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/gantt/cut.ts#L95)

Plain-data mapping row (subset of the Drizzle `cMDA` row).

## Properties

### dayId

> **dayId**: `string`

Defined in: [ui/src/api-server/gantt/cut.ts:97](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/gantt/cut.ts#L97)

***

### eventId

> **eventId**: `null` \| `string`

Defined in: [ui/src/api-server/gantt/cut.ts:96](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/gantt/cut.ts#L96)

***

### sortOrder?

> `optional` **sortOrder?**: `null` \| `number`

Defined in: [ui/src/api-server/gantt/cut.ts:98](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/gantt/cut.ts#L98)

***

### weekSplitMinutes?

> `optional` **weekSplitMinutes?**: `number`[] \| `null`

Defined in: [ui/src/api-server/gantt/cut.ts:100](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/gantt/cut.ts#L100)

Minutes per consecutive week for a split-across-weeks event (#768).
