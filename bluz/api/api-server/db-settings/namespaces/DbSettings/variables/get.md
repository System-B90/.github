[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-settings](../../../index.md) / [DbSettings](../index.md) / get

# Variable: get

> `const` **get**: (`name`, `options?`, `controller`) => `Promise`\<[`Setting`](../../../../../api-shared/types/settings/settings/type-aliases/Setting.md) \| `null`\> = `getDbSetting`

Defined in: [ui/src/api-server/db-settings.ts:179](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/db-settings.ts#L179)

## Parameters

### name

[`SettingName`](../../../../../api-shared/types/settings/settings/type-aliases/SettingName.md)

### options?

`FindOptions`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`Setting`](../../../../../api-shared/types/settings/settings/type-aliases/Setting.md) \| `null`\>
