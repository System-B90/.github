[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/event-context-menu](../index.md) / ContextMenuGuards

# Type Alias: ContextMenuGuards

> **ContextMenuGuards** = `object`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:66](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/schedule/event-context-menu/index.tsx#L66)

What stands between a menu entry and a write.

## Properties

### confirm

> **confirm**: (`message`, `options?`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:68](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/schedule/event-context-menu/index.tsx#L68)

Guards the bulk deletes; resolves false when the user backs out.

#### Parameters

##### message

`string`

##### options?

###### title?

`string`

#### Returns

`Promise`\<`boolean`\>

***

### confirmLockedEdit

> **confirmLockedEdit**: (`eventIds`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:73](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/schedule/event-context-menu/index.tsx#L73)

Asks before editing events another user has open (#775); resolves true
at once when none of them is locked.

#### Parameters

##### eventIds

[`EventId`](../../../../api-shared/types/event/type-aliases/EventId.md)[]

#### Returns

`Promise`\<`boolean`\>

***

### readOnly

> **readOnly**: `boolean`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:78](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/schedule/event-context-menu/index.tsx#L78)

A past iteration: the server rejects its writes, so only Copy (to paste
into a writable iteration) and navigation stay enabled.
