[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/room-settings/values](../index.md) / validateRoom

# Function: validateRoom()

> **validateRoom**(`values`, `requireName?`): [`ValidationResult`](../../../common/UseEntityForm/type-aliases/ValidationResult.md)

Defined in: [ui/src/components/settings-dialog/tabs/global/room-settings/values.ts:74](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/room-settings/values.ts#L74)

Only the name is required, and only for custom rooms — a Hive room's name is
read-only here, so editing one submits extended info alone. The caller
passes `requireName: false` in that case.

## Parameters

### values

[`RoomValues`](../type-aliases/RoomValues.md)

### requireName?

`boolean` = `true`

## Returns

[`ValidationResult`](../../../common/UseEntityForm/type-aliases/ValidationResult.md)
