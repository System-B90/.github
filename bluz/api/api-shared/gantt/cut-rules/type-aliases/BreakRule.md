[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-rules](../index.md) / BreakRule

# Type Alias: BreakRule

> **BreakRule** = `object`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:178](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-rules.ts#L178)

## Properties

### enabled

> **enabled**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:190](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-rules.ts#L190)

Off-switch for a rule that is specified but not yet actionable.

***

### maximumMinutes

> **maximumMinutes**: `number`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:186](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-rules.ts#L186)

Longest this break may be stretched to absorb leftover slack.

***

### minimumMinutes

> **minimumMinutes**: `number`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:184](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-rules.ts#L184)

Shortest acceptable length; below this the break is dropped entirely.

***

### preferredMinutes

> **preferredMinutes**: `number`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:182](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-rules.ts#L182)

Ideal length in minutes.

***

### priority

> **priority**: `number`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:180](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-rules.ts#L180)

Lower number = inserted first when slack is scarce.

***

### rationale

> **rationale**: `string`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:192](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-rules.ts#L192)

Why the rule exists — shown in docs and the preview's explanation.

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:188](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-rules.ts#L188)

Hebrew title given to the generated הפסקה event.
