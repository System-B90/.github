[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/room-settings/values](../index.md) / validateRoom

# Function: validateRoom()

> **validateRoom**(`values`, `requireName?`): [`ValidationResult`](../../../common/UseEntityForm/type-aliases/ValidationResult.md)

Defined in: [ui/src/components/settings-dialog/tabs/global/room-settings/values.ts:74](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/settings-dialog/tabs/global/room-settings/values.ts#L74)

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
