[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/OfflineProvider](../index.md) / OfflineContextState

# Type Alias: OfflineContextState

> **OfflineContextState** = `object`

Defined in: [ui/src/components/base/OfflineProvider.tsx:17](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OfflineProvider.tsx#L17)

## Properties

### captureEventBeforeEdit

> **captureEventBeforeEdit**: (`event`) => `void`

Defined in: [ui/src/components/base/OfflineProvider.tsx:23](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OfflineProvider.tsx#L23)

#### Parameters

##### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`void`

***

### captureInitialEvents

> **captureInitialEvents**: (`events`) => `void`

Defined in: [ui/src/components/base/OfflineProvider.tsx:24](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OfflineProvider.tsx#L24)

#### Parameters

##### events

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)[]

#### Returns

`void`

***

### default

> **default**: `boolean`

Defined in: [ui/src/components/base/OfflineProvider.tsx:18](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OfflineProvider.tsx#L18)

***

### getCapturedEvent

> **getCapturedEvent**: (`eventId`) => [`Event`](../../../../api-shared/types/event/type-aliases/Event.md) \| `null`

Defined in: [ui/src/components/base/OfflineProvider.tsx:27](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OfflineProvider.tsx#L27)

#### Parameters

##### eventId

[`EventId`](../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md) \| `null`

***

### getCapturedState

> **getCapturedState**: () => `Record`\<[`EventId`](../../../../api-shared/types/event/type-aliases/EventId.md), [`Event`](../../../../api-shared/types/event/type-aliases/Event.md)\>

Defined in: [ui/src/components/base/OfflineProvider.tsx:28](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OfflineProvider.tsx#L28)

#### Returns

`Record`\<[`EventId`](../../../../api-shared/types/event/type-aliases/EventId.md), [`Event`](../../../../api-shared/types/event/type-aliases/Event.md)\>

***

### isEventCreatedLocally

> **isEventCreatedLocally**: (`eventId`) => `boolean`

Defined in: [ui/src/components/base/OfflineProvider.tsx:30](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OfflineProvider.tsx#L30)

#### Parameters

##### eventId

[`EventId`](../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`boolean`

***

### markEventCreatedLocally

> **markEventCreatedLocally**: (`eventId`) => `void`

Defined in: [ui/src/components/base/OfflineProvider.tsx:29](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OfflineProvider.tsx#L29)

#### Parameters

##### eventId

[`EventId`](../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`void`

***

### offlineMode

> **offlineMode**: `boolean`

Defined in: [ui/src/components/base/OfflineProvider.tsx:19](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OfflineProvider.tsx#L19)

***

### purgeCapturedEvents

> **purgeCapturedEvents**: (`eventIds`) => `void`

Defined in: [ui/src/components/base/OfflineProvider.tsx:26](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OfflineProvider.tsx#L26)

#### Parameters

##### eventIds

[`EventId`](../../../../api-shared/types/event/type-aliases/EventId.md)[]

#### Returns

`void`

***

### purgeCapturedState

> **purgeCapturedState**: () => `void`

Defined in: [ui/src/components/base/OfflineProvider.tsx:25](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OfflineProvider.tsx#L25)

#### Returns

`void`

***

### pushDialogOpen

> **pushDialogOpen**: `boolean`

Defined in: [ui/src/components/base/OfflineProvider.tsx:21](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OfflineProvider.tsx#L21)

***

### setOfflineMode

> **setOfflineMode**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/OfflineProvider.tsx:20](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OfflineProvider.tsx#L20)

***

### setPushDialogOpen

> **setPushDialogOpen**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/OfflineProvider.tsx:22](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OfflineProvider.tsx#L22)
