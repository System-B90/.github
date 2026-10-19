[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/offline-dialogs/push-updates-dialog/utils](../index.md) / PushApi

# Type Alias: PushApi

> **PushApi** = `object`

Defined in: [ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts:185](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts#L185)

The three server operations the push dialog can perform per event. Injected
so the sync loop stays pure and unit-testable (no React / api-client).

## Properties

### createEvent

> **createEvent**: (`event`) => `Promise`\<`unknown`\>

Defined in: [ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts:186](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts#L186)

#### Parameters

##### event

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`Promise`\<`unknown`\>

***

### deleteEvent

> **deleteEvent**: (`eventId`) => `Promise`\<`unknown`\>

Defined in: [ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts:188](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts#L188)

#### Parameters

##### eventId

[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`Promise`\<`unknown`\>

***

### updateEvent

> **updateEvent**: (`event`) => `Promise`\<`unknown`\>

Defined in: [ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts:187](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts#L187)

#### Parameters

##### event

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`Promise`\<`unknown`\>
