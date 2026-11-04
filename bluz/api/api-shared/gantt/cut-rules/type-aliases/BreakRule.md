[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-rules](../index.md) / BreakRule

# Type Alias: BreakRule

> **BreakRule** = `object`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:179](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/gantt/cut-rules.ts#L179)

## Properties

### enabled

> **enabled**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:191](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/gantt/cut-rules.ts#L191)

Off-switch for a rule that is specified but not yet actionable.

***

### maximumMinutes

> **maximumMinutes**: `number`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:187](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/gantt/cut-rules.ts#L187)

Longest this break may be stretched to absorb leftover slack.

***

### minimumMinutes

> **minimumMinutes**: `number`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:185](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/gantt/cut-rules.ts#L185)

Shortest acceptable length; below this the break is dropped entirely.

***

### preferredMinutes

> **preferredMinutes**: `number`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:183](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/gantt/cut-rules.ts#L183)

Ideal length in minutes.

***

### priority

> **priority**: `number`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:181](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/gantt/cut-rules.ts#L181)

Lower number = inserted first when slack is scarce.

***

### rationale

> **rationale**: `string`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:193](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/gantt/cut-rules.ts#L193)

Why the rule exists — shown in docs and the preview's explanation.

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:189](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/gantt/cut-rules.ts#L189)

Hebrew title given to the generated הפסקה event.
