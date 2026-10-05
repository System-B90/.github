[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/personal-settings](../index.md) / PersonalSettings

# Type Alias: PersonalSettings

> **PersonalSettings** = `object`

Defined in: [ui/src/api-shared/types/personal-settings.ts:1](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/personal-settings.ts#L1)

## Properties

### aiApiToken

> **aiApiToken**: `string`

Defined in: [ui/src/api-shared/types/personal-settings.ts:22](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/personal-settings.ts#L22)

Per-user OpenRouter API key. Empty string means "use the server's
default key" (`OPENROUTER_API_KEY`), so a deployment with no personal
key still works when the server itself is configured.

***

### aiAssistantEnabled

> **aiAssistantEnabled**: `boolean`

Defined in: [ui/src/api-shared/types/personal-settings.ts:16](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/personal-settings.ts#L16)

Shows/hides the AI assistant FAB. On by default where AI is configured.

***

### aiModel

> **aiModel**: `string`

Defined in: [ui/src/api-shared/types/personal-settings.ts:27](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/personal-settings.ts#L27)

Personal model choice (#779); "" = the server's `AI_MODEL`. Honoured
only with the user's own key or when the server's backend lists it.

***

### favoriteOutsiders

> **favoriteOutsiders**: `string`[]

Defined in: [ui/src/api-shared/types/personal-settings.ts:4](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/personal-settings.ts#L4)

***

### googleCalendarEnabled

> **googleCalendarEnabled**: `boolean`

Defined in: [ui/src/api-shared/types/personal-settings.ts:9](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/personal-settings.ts#L9)

Opt-in two-way sync of the user's own events to their Google Calendar.
Off by default — Bluz must work fully in offline/no-internet deployments.

***

### googleCalendarSyncAllEvents

> **googleCalendarSyncAllEvents**: `boolean`

Defined in: [ui/src/api-shared/types/personal-settings.ts:14](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/personal-settings.ts#L14)

When on, sync every schedule event (not just ones the user instructs/
lectures in) to the user's Google Calendar. Requires googleCalendarEnabled.

***

### groups

> **groups**: `string`[]

Defined in: [ui/src/api-shared/types/personal-settings.ts:2](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/personal-settings.ts#L2)

***

### instructors

> **instructors**: `string`[]

Defined in: [ui/src/api-shared/types/personal-settings.ts:3](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/personal-settings.ts#L3)
