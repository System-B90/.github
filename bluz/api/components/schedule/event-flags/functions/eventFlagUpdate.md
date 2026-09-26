[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/event-flags](../index.md) / eventFlagUpdate

# Function: eventFlagUpdate()

> **eventFlagUpdate**(`key`, `value`): `Partial`\<[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)\>

Defined in: [ui/src/components/schedule/event-flags.ts:61](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-flags.ts#L61)

The patch that setting `key` to `value` implies. Turning "פיקטיבי" on also
detaches the event from Hive (#102): a fake event carries no subject,
module or lesson, so the flag is never a plain one-field write.

## Parameters

### key

[`EventFlagKey`](../type-aliases/EventFlagKey.md)

The flag being set.

### value

`boolean`

Its new value.

## Returns

`Partial`\<[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)\>

The fields to merge into the event.
