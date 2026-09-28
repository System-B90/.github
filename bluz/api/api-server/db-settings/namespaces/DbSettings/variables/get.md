[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-settings](../../../index.md) / [DbSettings](../index.md) / get

# Variable: get

> `const` **get**: (`name`, `options?`, `controller`) => `Promise`\<[`Setting`](../../../../../api-shared/types/settings/settings/type-aliases/Setting.md) \| `null`\> = `getDbSetting`

Defined in: [ui/src/api-server/db-settings.ts:154](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-server/db-settings.ts#L154)

## Parameters

### name

[`SettingName`](../../../../../api-shared/types/settings/settings/type-aliases/SettingName.md)

### options?

`FindOptions`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`Setting`](../../../../../api-shared/types/settings/settings/type-aliases/Setting.md) \| `null`\>
