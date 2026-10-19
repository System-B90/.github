[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/event-context-menu](../index.md) / ContextMenuGuards

# Type Alias: ContextMenuGuards

> **ContextMenuGuards** = `object`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:82](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/index.tsx#L82)

What stands between a menu entry and a write.

## Properties

### confirm

> **confirm**: (`message`, `options?`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:84](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/index.tsx#L84)

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

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:89](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/index.tsx#L89)

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

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:94](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/index.tsx#L94)

A past iteration: the server rejects its writes, so only Copy (to paste
into a writable iteration) and navigation stay enabled.
