[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/room-settings/values](../index.md) / validateRoom

# Function: validateRoom()

> **validateRoom**(`values`, `requireName?`): [`ValidationResult`](../../../common/UseEntityForm/type-aliases/ValidationResult.md)\<[`RoomValues`](../type-aliases/RoomValues.md)\>

Defined in: [ui/src/components/settings-dialog/tabs/global/room-settings/values.ts:76](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/settings-dialog/tabs/global/room-settings/values.ts#L76)

Only the name is required, and only for custom rooms — a Hive room's name is
read-only here, so editing one submits extended info alone. The caller
passes `requireName: false` in that case.

## Parameters

### values

[`RoomValues`](../type-aliases/RoomValues.md)

### requireName?

`boolean` = `true`

## Returns

[`ValidationResult`](../../../common/UseEntityForm/type-aliases/ValidationResult.md)\<[`RoomValues`](../type-aliases/RoomValues.md)\>
