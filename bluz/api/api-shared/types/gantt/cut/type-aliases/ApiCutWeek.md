[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCutWeek

# Type Alias: ApiCutWeek

> **ApiCutWeek** = `object`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:76](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L76)

A timeline week the cut dialog can offer for a single-week cut (#970).

## Properties

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:77](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L77)

***

### number

> **number**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:79](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L79)

1-based position on the timeline.

***

### startDate

> **startDate**: `null` \| `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:81](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L81)

The week's Sunday (YYYY-MM-DD), or null without a start date.
