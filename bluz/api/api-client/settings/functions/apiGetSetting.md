[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/settings](../index.md) / apiGetSetting

# Function: apiGetSetting()

> **apiGetSetting**\<`T`\>(`name`, `iterationId?`, `props?`): `Promise`\<`T`\>

Defined in: [ui/src/api-client/settings.ts:14](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-client/settings.ts#L14)

Settings live in the iteration's own database, so every read carries the
active iteration. An absent id means the current (writable) run.

## Type Parameters

### T

`T` = [`Setting`](../../../api-shared/types/settings/settings/type-aliases/Setting.md)

## Parameters

### name

`string`

### iterationId?

`string`

### props?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

## Returns

`Promise`\<`T`\>
