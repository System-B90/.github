[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCutWeek

# Type Alias: ApiCutWeek

> **ApiCutWeek** = `object`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:59](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L59)

A timeline week the cut dialog can offer for a single-week cut (#970).

## Properties

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:60](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L60)

***

### number

> **number**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:62](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L62)

1-based position on the timeline.

***

### startDate

> **startDate**: `null` \| `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:64](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L64)

The week's Sunday (YYYY-MM-DD), or null without a start date.
