[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/schedule-validation/types](../index.md) / RuleViolation

# Type Alias: RuleViolation

> **RuleViolation** = `object`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:63](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/types.ts#L63)

## Properties

### date

> **date**: `string`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:66](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/types.ts#L66)

Local civil date, `YYYY-MM-DD`.

***

### details

> **details**: `string`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:70](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/types.ts#L70)

Hebrew, the specifics. May be empty.

***

### eventIds

> **eventIds**: `string`[]

Defined in: [ui/src/api-shared/schedule-validation/types.ts:72](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/types.ts#L72)

Events to select when the row is opened; may be empty (e.g. a missing event).

***

### rule

> **rule**: [`ScheduleRuleId`](../../../schedule-rules/type-aliases/ScheduleRuleId.md)

Defined in: [ui/src/api-shared/schedule-validation/types.ts:64](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/types.ts#L64)

***

### summary

> **summary**: `string`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:68](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/types.ts#L68)

Hebrew, one line.
