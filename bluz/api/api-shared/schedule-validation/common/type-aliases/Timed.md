[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/schedule-validation/common](../index.md) / Timed

# Type Alias: Timed

> **Timed** = `object`

Defined in: [ui/src/api-shared/schedule-validation/common.ts:14](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/common.ts#L14)

A checked event with its instants and local day resolved once.

## Properties

### date

> **date**: `string`

Defined in: [ui/src/api-shared/schedule-validation/common.ts:19](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/common.ts#L19)

Local civil date of the start, `YYYY-MM-DD`.

***

### end

> **end**: `number`

Defined in: [ui/src/api-shared/schedule-validation/common.ts:17](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/common.ts#L17)

***

### event

> **event**: [`RuleCheckEvent`](../../types/type-aliases/RuleCheckEvent.md)

Defined in: [ui/src/api-shared/schedule-validation/common.ts:15](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/common.ts#L15)

***

### name

> **name**: `string`

Defined in: [ui/src/api-shared/schedule-validation/common.ts:23](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/common.ts#L23)

Normalized name (see [normalizeName](../functions/normalizeName.md)).

***

### start

> **start**: `number`

Defined in: [ui/src/api-shared/schedule-validation/common.ts:16](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/common.ts#L16)

***

### weekday

> **weekday**: `number`

Defined in: [ui/src/api-shared/schedule-validation/common.ts:21](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/common.ts#L21)

0 = Sunday … 6 = Saturday, local.
