[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/RoomsProvider](../index.md) / RoomsContextState

# Type Alias: RoomsContextState

> **RoomsContextState** = `object`

Defined in: [ui/src/components/base/RoomsProvider.tsx:23](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/RoomsProvider.tsx#L23)

## Properties

### addRoom

> **addRoom**: (`roomData`) => `Promise`\<`void`\>

Defined in: [ui/src/components/base/RoomsProvider.tsx:28](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/RoomsProvider.tsx#L28)

#### Parameters

##### roomData

`Omit`\<[`CustomRoom`](../../../../api-shared/types/room/type-aliases/CustomRoom.md), `"id"` \| `"source"`\>

#### Returns

`Promise`\<`void`\>

***

### default

> **default**: `boolean`

Defined in: [ui/src/components/base/RoomsProvider.tsx:24](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/RoomsProvider.tsx#L24)

***

### deleteRoom

> **deleteRoom**: (`roomId`) => `Promise`\<`void`\>

Defined in: [ui/src/components/base/RoomsProvider.tsx:30](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/RoomsProvider.tsx#L30)

#### Parameters

##### roomId

`string`

#### Returns

`Promise`\<`void`\>

***

### getRoom

> **getRoom**: (`id`) => `null` \| [`Room`](../../../../api-shared/types/room/type-aliases/Room.md)

Defined in: [ui/src/components/base/RoomsProvider.tsx:27](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/RoomsProvider.tsx#L27)

#### Parameters

##### id

[`RoomLike`](../../../../api-shared/types/room/type-aliases/RoomLike.md)

#### Returns

`null` \| [`Room`](../../../../api-shared/types/room/type-aliases/Room.md)

***

### isLoading

> **isLoading**: `boolean`

Defined in: [ui/src/components/base/RoomsProvider.tsx:26](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/RoomsProvider.tsx#L26)

***

### rooms

> **rooms**: [`Room`](../../../../api-shared/types/room/type-aliases/Room.md)[]

Defined in: [ui/src/components/base/RoomsProvider.tsx:25](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/RoomsProvider.tsx#L25)

***

### updateRoom

> **updateRoom**: (`room`) => `Promise`\<`void`\>

Defined in: [ui/src/components/base/RoomsProvider.tsx:29](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/RoomsProvider.tsx#L29)

#### Parameters

##### room

[`CustomRoom`](../../../../api-shared/types/room/type-aliases/CustomRoom.md)

#### Returns

`Promise`\<`void`\>

***

### updateRoomExtendedInfo

> **updateRoomExtendedInfo**: (`roomId`, `roomSource`, `extendedInfo`) => `Promise`\<`void`\>

Defined in: [ui/src/components/base/RoomsProvider.tsx:31](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/RoomsProvider.tsx#L31)

#### Parameters

##### roomId

[`RoomId`](../../../../api-shared/types/room/type-aliases/RoomId.md)

##### roomSource

[`RoomSource`](../../../../api-shared/types/room/enumerations/RoomSource.md)

##### extendedInfo

[`RoomExtendedInfo`](../../../../api-shared/types/room/type-aliases/RoomExtendedInfo.md)

#### Returns

`Promise`\<`void`\>
