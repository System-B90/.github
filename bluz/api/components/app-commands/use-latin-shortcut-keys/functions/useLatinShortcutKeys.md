[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-commands/use-latin-shortcut-keys](../index.md) / useLatinShortcutKeys

# Function: useLatinShortcutKeys()

> **useLatinShortcutKeys**(): `void`

Defined in: [ui/src/components/app-commands/use-latin-shortcut-keys.ts:39](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/components/app-commands/use-latin-shortcut-keys.ts#L39)

Makes Ctrl/Cmd+letter shortcuts layout-independent (#989). The palette and
the calendar match `KeyboardEvent.key`, so on the Hebrew layout Ctrl+Z
arrived as "ז" and undo, redo, copy, cut, paste and Ctrl+G did nothing.
Such a keystroke is swapped, before anything else sees it, for a copy
carrying the Latin key. Text fields keep the original: the browser's own
editing shortcuts already work there.

## Returns

`void`
