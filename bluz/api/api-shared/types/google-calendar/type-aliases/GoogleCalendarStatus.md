[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/google-calendar](../index.md) / GoogleCalendarStatus

# Type Alias: GoogleCalendarStatus

> **GoogleCalendarStatus** = `object`

Defined in: [ui/src/api-shared/types/google-calendar.ts:69](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L69)

Client-safe view of the connection state — no tokens.

## Properties

### calendar?

> `optional` **calendar?**: [`GoogleCalendarSelection`](GoogleCalendarSelection.md)

Defined in: [ui/src/api-shared/types/google-calendar.ts:78](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L78)

Present while connected.

***

### clientId

> **clientId**: `string`

Defined in: [ui/src/api-shared/types/google-calendar.ts:74](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L74)

Public OAuth client id the browser uses for the GIS "Continue with Google" popup.

***

### configured

> **configured**: `boolean`

Defined in: [ui/src/api-shared/types/google-calendar.ts:70](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L70)

***

### connected

> **connected**: `boolean`

Defined in: [ui/src/api-shared/types/google-calendar.ts:71](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L71)

***

### enabled

> **enabled**: `boolean`

Defined in: [ui/src/api-shared/types/google-calendar.ts:72](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L72)

***

### scopes

> **scopes**: `string`[]

Defined in: [ui/src/api-shared/types/google-calendar.ts:76](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L76)

OAuth scopes the GIS popup must request.
