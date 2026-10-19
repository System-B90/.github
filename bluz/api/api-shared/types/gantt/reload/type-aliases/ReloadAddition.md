[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/reload](../index.md) / ReloadAddition

# Type Alias: ReloadAddition

> **ReloadAddition** = `object`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:16](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L16)

A planned occurrence that has no schedule event yet — will be created.

## Properties

### endTime

> **endTime**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:24](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L24)

ISO datetime.

***

### ganttEventId

> **ganttEventId**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:17](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L17)

***

### occurrenceDate

> **occurrenceDate**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:19](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L19)

yyyy-MM-dd

***

### parked?

> `optional` **parked?**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:29](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L29)

The user deleted this occurrence from the schedule since the cut, so it
is re-created in the unassigned-events box instead of on the grid.

***

### startTime

> **startTime**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:22](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L22)

ISO datetime.

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:20](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L20)
