[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-settings](../../../index.md) / [DbSettings](../index.md) / set

# Variable: set

> `const` **set**: (`name`, `setting`, `options?`, `controller`, `broadcast`) => `Promise`\<`void`\> = `setDbSetting`

Defined in: [ui/src/api-server/db-settings.ts:180](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/db-settings.ts#L180)

## Parameters

### name

[`SettingName`](../../../../../api-shared/types/settings/settings/type-aliases/SettingName.md)

### setting

`Partial`\<[`Setting`](../../../../../api-shared/types/settings/settings/type-aliases/Setting.md)\>

### options?

`UpdateOptions`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

### broadcast?

`boolean` = `true`

## Returns

`Promise`\<`void`\>
