[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/schedule-validation/types](../index.md) / RuleCheck

# Type Alias: RuleCheck

> **RuleCheck** = `object`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:75](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-validation/types.ts#L75)

## Properties

### id

> **id**: [`ScheduleRuleId`](../../../schedule-rules/type-aliases/ScheduleRuleId.md)

Defined in: [ui/src/api-shared/schedule-validation/types.ts:76](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-validation/types.ts#L76)

***

### needs?

> `optional` **needs?**: `ReadonlyArray`\<[`RuleCheckNeed`](RuleCheckNeed.md)\>

Defined in: [ui/src/api-shared/schedule-validation/types.ts:77](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-validation/types.ts#L77)

***

### run

> **run**: (`events`, `context`) => [`RuleViolation`](RuleViolation.md)[]

Defined in: [ui/src/api-shared/schedule-validation/types.ts:78](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-validation/types.ts#L78)

#### Parameters

##### events

`ReadonlyArray`\<[`RuleCheckEvent`](RuleCheckEvent.md)\>

##### context

[`RuleCheckContext`](RuleCheckContext.md)

#### Returns

[`RuleViolation`](RuleViolation.md)[]
