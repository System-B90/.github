[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-component/event-colors](../index.md) / resolveEventDefaultColor

# Function: resolveEventDefaultColor()

> **resolveEventDefaultColor**(`event`, `subject`, `fallback`): `string`

Defined in: [ui/src/components/schedule/event-component/event-colors.ts:12](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/schedule/event-component/event-colors.ts#L12)

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
