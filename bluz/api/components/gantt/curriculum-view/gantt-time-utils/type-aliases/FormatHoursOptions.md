[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-time-utils](../index.md) / FormatHoursOptions

# Type Alias: FormatHoursOptions

> **FormatHoursOptions** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:105](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L105)

## Properties

### maximumFractionDigits?

> `optional` **maximumFractionDigits?**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:107](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L107)

Decimal places in decimal mode (clock mode is always `h:mm`).

***

### unit?

> `optional` **unit?**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:112](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L112)

Append the unit (`ש׳`, or `דק׳` in minutes mode), so a duration never
reads as a clock time (#813).
