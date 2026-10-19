[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-component/event-colors](../index.md) / resolveEventColor

# Function: resolveEventColor()

> **resolveEventColor**(`event`, `subject`, `lookups`, `fallback`): `string`

Defined in: [ui/src/components/schedule/event-component/event-colors.ts:30](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/event-component/event-colors.ts#L30)

Resolves the display color for a calendar event, including per-event overrides.
`event.color` stores an ID (a custom color ID or a Hive subject ID), not a hex
string, so it must be looked up before use.
Resolution order: custom color → Hive subject color (by ID) → default color.

## Parameters

### event

`Partial`\<[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)\>

### subject

\{ `color?`: `string`; \} \| `undefined`

### lookups

#### getCustomColor

(`id`) => \{ `hex`: `string`; \} \| `null` \| `undefined`

#### getSubject

(`id`) => \{ `color?`: `string`; \} \| `undefined`

### fallback

`string`

## Returns

`string`
