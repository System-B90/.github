[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/google-calendar](../index.md) / GoogleCalendarStatus

# Type Alias: GoogleCalendarStatus

> **GoogleCalendarStatus** = `object`

Defined in: [ui/src/api-shared/types/google-calendar.ts:75](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/google-calendar.ts#L75)

Client-safe view of the connection state — no tokens.

## Properties

### calendar?

> `optional` **calendar?**: [`GoogleCalendarSelection`](GoogleCalendarSelection.md)

Defined in: [ui/src/api-shared/types/google-calendar.ts:86](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/google-calendar.ts#L86)

Present while connected.

***

### clientId

> **clientId**: `string`

Defined in: [ui/src/api-shared/types/google-calendar.ts:82](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/google-calendar.ts#L82)

Public OAuth client id the browser uses for the GIS "Continue with Google" popup.

***

### configured

> **configured**: `boolean`

Defined in: [ui/src/api-shared/types/google-calendar.ts:76](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/google-calendar.ts#L76)

***

### connected

> **connected**: `boolean`

Defined in: [ui/src/api-shared/types/google-calendar.ts:77](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/google-calendar.ts#L77)

***

### enabled

> **enabled**: `boolean`

Defined in: [ui/src/api-shared/types/google-calendar.ts:80](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/google-calendar.ts#L80)

***

### needsReauth?

> `optional` **needsReauth?**: `boolean`

Defined in: [ui/src/api-shared/types/google-calendar.ts:79](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/google-calendar.ts#L79)

A link exists but its Google token expired or was revoked; `connected` is false (#914).

***

### scopes

> **scopes**: `string`[]

Defined in: [ui/src/api-shared/types/google-calendar.ts:84](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/google-calendar.ts#L84)

OAuth scopes the GIS popup must request.
