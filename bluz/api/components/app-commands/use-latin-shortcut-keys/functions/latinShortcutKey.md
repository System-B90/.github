[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-commands/use-latin-shortcut-keys](../index.md) / latinShortcutKey

# Function: latinShortcutKey()

> **latinShortcutKey**(`e`): `string` \| `null`

Defined in: [ui/src/components/app-commands/use-latin-shortcut-keys.ts:11](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/app-commands/use-latin-shortcut-keys.ts#L11)

The Latin letter a Ctrl/Cmd keystroke stands for when the active layout
types something else there, e.g. "z" for the "ז" the Hebrew layout reports
for Ctrl+Z. `null` when `key` is already Latin or the key is not a letter.

## Parameters

### e

`Pick`\<`KeyboardEvent`, `"altKey"` \| `"code"` \| `"ctrlKey"` \| `"key"` \| `"metaKey"`\>

## Returns

`string` \| `null`
