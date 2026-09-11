[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-component/event-colors](../index.md) / resolveColorById

# Function: resolveColorById()

> **resolveColorById**(`colorId`, `lookups`): \{ `hex`: `string`; `label`: `string`; \} \| `undefined`

Defined in: [ui/src/components/schedule/event-component/event-colors.ts:56](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/event-component/event-colors.ts#L56)

Resolves a color ID (a custom color ID or a Hive subject ID) to its hex value
and display label. Resolution order: custom color → Hive subject.

## Parameters

### colorId

`string`

### lookups

#### getCustomColor

(`id`) => \{ `hex`: `string`; `name`: `string`; \} \| `null` \| `undefined`

#### getSubject

(`id`) => \{ `color?`: `string`; `displayName?`: `string`; `name?`: `string`; \} \| `undefined`

## Returns

\{ `hex`: `string`; `label`: `string`; \} \| `undefined`
