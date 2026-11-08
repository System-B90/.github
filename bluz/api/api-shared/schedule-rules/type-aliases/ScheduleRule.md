[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/schedule-rules](../index.md) / ScheduleRule

# Type Alias: ScheduleRule

> **ScheduleRule** = `object`

Defined in: [ui/src/api-shared/schedule-rules.ts:41](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/schedule-rules.ts#L41)

## Properties

### checkedBy?

> `optional` **checkedBy?**: `string`

Defined in: [ui/src/api-shared/schedule-rules.ts:52](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/schedule-rules.ts#L52)

Where the app checks it automatically, if anywhere.

***

### description

> **description**: `string`

Defined in: [ui/src/api-shared/schedule-rules.ts:48](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/schedule-rules.ts#L48)

What the rule means and why, in Hebrew.

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/schedule-rules.ts:42](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/schedule-rules.ts#L42)

***

### points?

> `optional` **points?**: `ReadonlyArray`\<`string`\>

Defined in: [ui/src/api-shared/schedule-rules.ts:50](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/schedule-rules.ts#L50)

Optional sub-points (cases, exceptions).

***

### section

> **section**: [`RuleSectionId`](RuleSectionId.md)

Defined in: [ui/src/api-shared/schedule-rules.ts:43](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/schedule-rules.ts#L43)

***

### tier?

> `optional` **tier?**: [`RuleTier`](RuleTier.md)

Defined in: [ui/src/api-shared/schedule-rules.ts:44](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/schedule-rules.ts#L44)

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/schedule-rules.ts:46](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/schedule-rules.ts#L46)

Short Hebrew name.

***

### violationLabel?

> `optional` **violationLabel?**: `string`

Defined in: [ui/src/api-shared/schedule-rules.ts:54](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/schedule-rules.ts#L54)

Short Hebrew label for a violation of this rule, when the app reports one.
