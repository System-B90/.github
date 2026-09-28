[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-component/event-colors](../index.md) / resolveEventDefaultColor

# Function: resolveEventDefaultColor()

> **resolveEventDefaultColor**(`event`, `subject`, `fallback`): `string`

Defined in: [ui/src/components/schedule/event-component/event-colors.ts:12](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/components/schedule/event-component/event-colors.ts#L12)

Resolves the default display color for a calendar event (ignoring per-event overrides).
Resolution order: Prayer default → Hive subject color → fallback.

## Parameters

### event

`Partial`\<[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)\>

### subject

\{ `color?`: `string`; \} \| `undefined`

### fallback

`string`

## Returns

`string`
