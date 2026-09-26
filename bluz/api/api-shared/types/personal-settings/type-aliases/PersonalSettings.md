[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/personal-settings](../index.md) / PersonalSettings

# Type Alias: PersonalSettings

> **PersonalSettings** = `object`

Defined in: [ui/src/api-shared/types/personal-settings.ts:1](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/personal-settings.ts#L1)

## Properties

### aiApiToken

> **aiApiToken**: `string`

Defined in: [ui/src/api-shared/types/personal-settings.ts:22](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/personal-settings.ts#L22)

Per-user OpenRouter API key. Empty string means "use the server's
default key" (`OPENROUTER_API_KEY`), so a deployment with no personal
key still works when the server itself is configured.

***

### aiAssistantEnabled

> **aiAssistantEnabled**: `boolean`

Defined in: [ui/src/api-shared/types/personal-settings.ts:16](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/personal-settings.ts#L16)

Shows/hides the AI assistant FAB. On by default where AI is configured.

***

### favoriteOutsiders

> **favoriteOutsiders**: `string`[]

Defined in: [ui/src/api-shared/types/personal-settings.ts:4](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/personal-settings.ts#L4)

***

### googleCalendarEnabled

> **googleCalendarEnabled**: `boolean`

Defined in: [ui/src/api-shared/types/personal-settings.ts:9](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/personal-settings.ts#L9)

Opt-in two-way sync of the user's own events to their Google Calendar.
Off by default — Bluz must work fully in offline/no-internet deployments.

***

### googleCalendarSyncAllEvents

> **googleCalendarSyncAllEvents**: `boolean`

Defined in: [ui/src/api-shared/types/personal-settings.ts:14](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/personal-settings.ts#L14)

When on, sync every schedule event (not just ones the user instructs/
lectures in) to the user's Google Calendar. Requires googleCalendarEnabled.

***

### groups

> **groups**: `string`[]

Defined in: [ui/src/api-shared/types/personal-settings.ts:2](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/personal-settings.ts#L2)

***

### instructors

> **instructors**: `string`[]

Defined in: [ui/src/api-shared/types/personal-settings.ts:3](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/personal-settings.ts#L3)
