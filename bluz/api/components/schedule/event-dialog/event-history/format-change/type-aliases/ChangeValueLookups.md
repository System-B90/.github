[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/event-dialog/event-history/format-change](../index.md) / ChangeValueLookups

# Type Alias: ChangeValueLookups

> **ChangeValueLookups** = `object`

Defined in: [ui/src/components/schedule/event-dialog/event-history/format-change.ts:12](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/event-dialog/event-history/format-change.ts#L12)

Renders a logged field value for humans. The log stores raw wire values
(epoch ms for dates, id arrays for people/rooms/courses), so the panel needs
name lookups injected — kept as a plain callback map so this stays pure and
testable without React providers.

## Properties

### colorInfo

> **colorInfo**: (`id`) => \{ `hex`: `string`; `label`: `string`; \} \| `undefined`

Defined in: [ui/src/components/schedule/event-dialog/event-history/format-change.ts:13](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/event-dialog/event-history/format-change.ts#L13)

#### Parameters

##### id

`string`

#### Returns

\{ `hex`: `string`; `label`: `string`; \} \| `undefined`

***

### courseName

> **courseName**: (`id`) => `string` \| `undefined`

Defined in: [ui/src/components/schedule/event-dialog/event-history/format-change.ts:14](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/event-dialog/event-history/format-change.ts#L14)

#### Parameters

##### id

`string`

#### Returns

`string` \| `undefined`

***

### instructorName

> **instructorName**: (`id`) => `string` \| `undefined`

Defined in: [ui/src/components/schedule/event-dialog/event-history/format-change.ts:15](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/event-dialog/event-history/format-change.ts#L15)

#### Parameters

##### id

`number`

#### Returns

`string` \| `undefined`

***

### roomName

> **roomName**: (`id`) => `string` \| `undefined`

Defined in: [ui/src/components/schedule/event-dialog/event-history/format-change.ts:16](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/event-dialog/event-history/format-change.ts#L16)

#### Parameters

##### id

`string`

#### Returns

`string` \| `undefined`
