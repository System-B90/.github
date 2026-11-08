[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/app-onboarding/schedule/tutorials](../index.md) / ScheduleTutorial

# Type Alias: ScheduleTutorial

> **ScheduleTutorial** = `object`

Defined in: [ui/src/components/app-onboarding/schedule/tutorials.ts:13](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/app-onboarding/schedule/tutorials.ts#L13)

The schedule's tutorials: one tour per job a planner does on this screen.

A single first-run tour cannot teach a whole screen — it either skims or
runs for twenty steps. So the intro only orients, and each task gets a short
tour of its own, started from the help panel or the command palette when
the user is about to do that task.

This list is the one place a tutorial's name and purpose are written: the
tour's card title, its help-panel entry and its palette command all read
from here, so they cannot drift apart.

## Properties

### id

> **id**: `string`

Defined in: [ui/src/components/app-onboarding/schedule/tutorials.ts:15](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/app-onboarding/schedule/tutorials.ts#L15)

The tour's id. It is the persistence key — never rename one.

***

### keywords

> **keywords**: `ReadonlyArray`\<`string`\>

Defined in: [ui/src/components/app-onboarding/schedule/tutorials.ts:20](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/app-onboarding/schedule/tutorials.ts#L20)

Extra palette match tokens: English aliases and synonyms.

***

### summary

> **summary**: `string`

Defined in: [ui/src/components/app-onboarding/schedule/tutorials.ts:18](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/app-onboarding/schedule/tutorials.ts#L18)

What the tutorial is for, in one sentence.

***

### title

> **title**: `string`

Defined in: [ui/src/components/app-onboarding/schedule/tutorials.ts:16](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/app-onboarding/schedule/tutorials.ts#L16)
