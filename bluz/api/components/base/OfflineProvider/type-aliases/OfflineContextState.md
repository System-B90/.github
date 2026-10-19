[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/OfflineProvider](../index.md) / OfflineContextState

# Type Alias: OfflineContextState

> **OfflineContextState** = `object`

Defined in: [ui/src/components/base/OfflineProvider.tsx:37](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L37)

## Properties

### activeDraft

> **activeDraft**: [`ActiveDraft`](ActiveDraft.md) \| `null`

Defined in: [ui/src/components/base/OfflineProvider.tsx:52](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L52)

The draft being edited, while the offline session is a draft session.

***

### activeTemplate

> **activeTemplate**: [`ActiveTemplate`](ActiveTemplate.md) \| `null`

Defined in: [ui/src/components/base/OfflineProvider.tsx:70](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L70)

The week template being edited, while the session is a template session.

***

### beginDraftSession

> **beginDraftSession**: (`draft`, `baseline`, `createdIds`) => `void`

Defined in: [ui/src/components/base/OfflineProvider.tsx:59](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L59)

Starts (or restarts) an offline session for a draft: `baseline` is
what the server holds for the draft's range, so leaving offline mode
diffs the draft against the live schedule. `createdIds` are the draft's
events the server does not have.

#### Parameters

##### draft

[`ActiveDraft`](ActiveDraft.md)

##### baseline

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)[]

##### createdIds

[`EventId`](../../../../api-shared/types/event/type-aliases/EventId.md)[]

#### Returns

`void`

***

### beginTemplateSession

> **beginTemplateSession**: (`template`, `events`) => `void`

Defined in: [ui/src/components/base/OfflineProvider.tsx:76](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L76)

Starts an offline session editing a week template. Its stored events
are both what is shown and the baseline; nothing is ever diffed against
the live schedule.

#### Parameters

##### template

[`ActiveTemplate`](ActiveTemplate.md)

##### events

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)[]

#### Returns

`void`

***

### captureEventBeforeEdit

> **captureEventBeforeEdit**: (`event`) => `void`

Defined in: [ui/src/components/base/OfflineProvider.tsx:43](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L43)

#### Parameters

##### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`void`

***

### captureInitialEvents

> **captureInitialEvents**: (`events`) => `void`

Defined in: [ui/src/components/base/OfflineProvider.tsx:44](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L44)

#### Parameters

##### events

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)[]

#### Returns

`void`

***

### default

> **default**: `boolean`

Defined in: [ui/src/components/base/OfflineProvider.tsx:38](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L38)

***

### getCapturedEvent

> **getCapturedEvent**: (`eventId`) => [`Event`](../../../../api-shared/types/event/type-aliases/Event.md) \| `null`

Defined in: [ui/src/components/base/OfflineProvider.tsx:47](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L47)

#### Parameters

##### eventId

[`EventId`](../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md) \| `null`

***

### getCapturedState

> **getCapturedState**: () => `Record`\<[`EventId`](../../../../api-shared/types/event/type-aliases/EventId.md), [`Event`](../../../../api-shared/types/event/type-aliases/Event.md)\>

Defined in: [ui/src/components/base/OfflineProvider.tsx:48](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L48)

#### Returns

`Record`\<[`EventId`](../../../../api-shared/types/event/type-aliases/EventId.md), [`Event`](../../../../api-shared/types/event/type-aliases/Event.md)\>

***

### isEventCreatedLocally

> **isEventCreatedLocally**: (`eventId`) => `boolean`

Defined in: [ui/src/components/base/OfflineProvider.tsx:50](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L50)

#### Parameters

##### eventId

[`EventId`](../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`boolean`

***

### markEventCreatedLocally

> **markEventCreatedLocally**: (`eventId`) => `void`

Defined in: [ui/src/components/base/OfflineProvider.tsx:49](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L49)

#### Parameters

##### eventId

[`EventId`](../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`void`

***

### moveTemplateSession

> **moveTemplateSession**: (`weekStart`) => `void`

Defined in: [ui/src/components/base/OfflineProvider.tsx:78](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L78)

Records that the template session's events now sit in another week.

#### Parameters

##### weekStart

`string`

#### Returns

`void`

***

### offlineMode

> **offlineMode**: `boolean`

Defined in: [ui/src/components/base/OfflineProvider.tsx:39](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L39)

***

### purgeCapturedEvents

> **purgeCapturedEvents**: (`eventIds`) => `void`

Defined in: [ui/src/components/base/OfflineProvider.tsx:46](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L46)

#### Parameters

##### eventIds

[`EventId`](../../../../api-shared/types/event/type-aliases/EventId.md)[]

#### Returns

`void`

***

### purgeCapturedState

> **purgeCapturedState**: () => `void`

Defined in: [ui/src/components/base/OfflineProvider.tsx:45](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L45)

#### Returns

`void`

***

### pushDialogOpen

> **pushDialogOpen**: `boolean`

Defined in: [ui/src/components/base/OfflineProvider.tsx:41](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L41)

***

### setOfflineMode

> **setOfflineMode**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/OfflineProvider.tsx:40](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L40)

***

### setPushDialogOpen

> **setPushDialogOpen**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/OfflineProvider.tsx:42](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L42)

***

### takeProvidedBaseline

> **takeProvidedBaseline**: () => `boolean`

Defined in: [ui/src/components/base/OfflineProvider.tsx:68](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/OfflineProvider.tsx#L68)

True once per session when the baseline was supplied by
`beginDraftSession`, so the calendar must not capture its own.

#### Returns

`boolean`
