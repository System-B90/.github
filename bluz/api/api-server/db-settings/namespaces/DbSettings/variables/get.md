[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-settings](../../../index.md) / [DbSettings](../index.md) / get

# Variable: get

> `const` **get**: (`name`, `options?`, `controller`) => `Promise`\<[`Setting`](../../../../../api-shared/types/settings/settings/type-aliases/Setting.md) \| `null`\> = `getDbSetting`

Defined in: [ui/src/api-server/db-settings.ts:179](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/db-settings.ts#L179)

## Parameters

### name

[`SettingName`](../../../../../api-shared/types/settings/settings/type-aliases/SettingName.md)

### options?

`FindOptions`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`Setting`](../../../../../api-shared/types/settings/settings/type-aliases/Setting.md) \| `null`\>
