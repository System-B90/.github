[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-time-utils](../index.md) / FormatHoursOptions

# Type Alias: FormatHoursOptions

> **FormatHoursOptions** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:105](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L105)

## Properties

### maximumFractionDigits?

> `optional` **maximumFractionDigits?**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:107](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L107)

Decimal places in decimal mode (clock mode is always `h:mm`).

***

### unit?

> `optional` **unit?**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:112](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L112)

Append the unit (`ש׳`, or `דק׳` in minutes mode), so a duration never
reads as a clock time (#813).
