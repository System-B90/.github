[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCutWeek

# Type Alias: ApiCutWeek

> **ApiCutWeek** = `object`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:88](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-shared/types/gantt/cut.ts#L88)

A timeline week the cut dialog can offer for a single-week cut (#970).

## Properties

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:89](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-shared/types/gantt/cut.ts#L89)

***

### number

> **number**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:91](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-shared/types/gantt/cut.ts#L91)

1-based position on the timeline.

***

### startDate

> **startDate**: `null` \| `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:93](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-shared/types/gantt/cut.ts#L93)

The week's Sunday (YYYY-MM-DD), or null without a start date.
