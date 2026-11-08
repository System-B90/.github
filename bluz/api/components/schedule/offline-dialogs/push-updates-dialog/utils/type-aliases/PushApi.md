[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/offline-dialogs/push-updates-dialog/utils](../index.md) / PushApi

# Type Alias: PushApi

> **PushApi** = `object`

Defined in: [ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts:191](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts#L191)

The three server operations the push dialog can perform per event. Injected
so the sync loop stays pure and unit-testable (no React / api-client).

## Properties

### createEvent

> **createEvent**: (`event`) => `Promise`\<`unknown`\>

Defined in: [ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts:192](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts#L192)

#### Parameters

##### event

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`Promise`\<`unknown`\>

***

### deleteEvent

> **deleteEvent**: (`eventId`) => `Promise`\<`unknown`\>

Defined in: [ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts:194](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts#L194)

#### Parameters

##### eventId

[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`Promise`\<`unknown`\>

***

### updateEvent

> **updateEvent**: (`event`) => `Promise`\<`unknown`\>

Defined in: [ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts:193](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts#L193)

#### Parameters

##### event

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`Promise`\<`unknown`\>
