[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-time-utils](../index.md) / FormatHoursOptions

# Type Alias: FormatHoursOptions

> **FormatHoursOptions** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:91](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L91)

## Properties

### maximumFractionDigits?

> `optional` **maximumFractionDigits?**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:93](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L93)

Decimal places in decimal mode (clock mode is always `h:mm`).

***

### unit?

> `optional` **unit?**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:98](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L98)

Append the unit (`ש׳`, or `דק׳` in minutes mode), so a duration never
reads as a clock time (#813).
