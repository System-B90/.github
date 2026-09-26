[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-settings](../../../index.md) / [DbSettings](../index.md) / set

# Variable: set

> `const` **set**: (`name`, `setting`, `options?`, `controller`) => `Promise`\<`void`\> = `setDbSetting`

Defined in: [ui/src/api-server/db-settings.ts:131](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/db-settings.ts#L131)

## Parameters

### name

[`SettingName`](../../../../../api-shared/types/settings/settings/type-aliases/SettingName.md)

### setting

`Partial`\<[`Setting`](../../../../../api-shared/types/settings/settings/type-aliases/Setting.md)\>

### options?

`UpdateOptions`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<`void`\>
