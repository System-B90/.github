[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/event-context-menu](../index.md) / ContextMenuGuards

# Type Alias: ContextMenuGuards

> **ContextMenuGuards** = `object`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:86](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/event-context-menu/index.tsx#L86)

What stands between a menu entry and a write.

## Properties

### confirm

> **confirm**: (`message`, `options?`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:88](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/event-context-menu/index.tsx#L88)

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

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:93](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/event-context-menu/index.tsx#L93)

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

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:98](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/event-context-menu/index.tsx#L98)

A past iteration: the server rejects its writes, so only Copy (to paste
into a writable iteration) and navigation stay enabled.
