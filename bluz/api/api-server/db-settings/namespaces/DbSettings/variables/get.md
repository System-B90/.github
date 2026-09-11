[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-settings](../../../index.md) / [DbSettings](../index.md) / get

# Variable: get

> `const` **get**: (`name`, `options?`, `controller`) => `Promise`\<[`Setting`](../../../../../api-shared/types/settings/settings/type-aliases/Setting.md) \| `null`\> = `getDbSetting`

Defined in: [ui/src/api-server/db-settings.ts:127](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/db-settings.ts#L127)

## Parameters

### name

[`SettingName`](../../../../../api-shared/types/settings/settings/type-aliases/SettingName.md)

### options?

`FindOptions`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`Setting`](../../../../../api-shared/types/settings/settings/type-aliases/Setting.md) \| `null`\>
