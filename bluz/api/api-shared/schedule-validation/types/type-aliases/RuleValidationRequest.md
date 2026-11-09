[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/schedule-validation/types](../index.md) / RuleValidationRequest

# Type Alias: RuleValidationRequest

> **RuleValidationRequest** = `object`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:82](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/types.ts#L82)

Body of `POST /api/calendar/validate/[ruleId]`: one source, as for the alignment route.

## Properties

### draftId?

> `optional` **draftId?**: `string`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:85](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/types.ts#L85)

***

### end?

> `optional` **end?**: `string`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:84](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/types.ts#L84)

***

### events?

> `optional` **events?**: [`DbEventDocument`](../../../types/event/type-aliases/DbEventDocument.md)[]

Defined in: [ui/src/api-shared/schedule-validation/types.ts:86](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/types.ts#L86)

***

### start?

> `optional` **start?**: `string`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:83](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/types.ts#L83)
