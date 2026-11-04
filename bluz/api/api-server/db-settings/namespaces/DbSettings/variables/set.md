[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-settings](../../../index.md) / [DbSettings](../index.md) / set

# Variable: set

> `const` **set**: (`name`, `setting`, `options?`, `controller`, `broadcast`) => `Promise`\<`void`\> = `setDbSetting`

Defined in: [ui/src/api-server/db-settings.ts:180](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/db-settings.ts#L180)

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
