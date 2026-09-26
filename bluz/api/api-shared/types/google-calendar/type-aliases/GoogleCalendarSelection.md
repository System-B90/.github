[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/google-calendar](../index.md) / GoogleCalendarSelection

# Type Alias: GoogleCalendarSelection

> **GoogleCalendarSelection** = `object`

Defined in: [ui/src/api-shared/types/google-calendar.ts:57](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L57)

Client-safe view of the linked calendar — no tokens.

## Properties

### accessRole?

> `optional` **accessRole?**: [`GoogleCalendarAccessRole`](GoogleCalendarAccessRole.md)

Defined in: [ui/src/api-shared/types/google-calendar.ts:60](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L60)

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types/google-calendar.ts:58](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L58)

***

### iterationId?

> `optional` **iterationId?**: [`IterationId`](../../iteration/type-aliases/IterationId.md)

Defined in: [ui/src/api-shared/types/google-calendar.ts:61](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L61)

***

### iterationLabel?

> `optional` **iterationLabel?**: `string`

Defined in: [ui/src/api-shared/types/google-calendar.ts:63](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L63)

Label of `iterationId`, resolved server-side for display.

***

### linkedUsers

> **linkedUsers**: `number`

Defined in: [ui/src/api-shared/types/google-calendar.ts:65](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L65)

How many Bluz users (including this one) mirror into this same calendar.

***

### summary

> **summary**: `string`

Defined in: [ui/src/api-shared/types/google-calendar.ts:59](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L59)
