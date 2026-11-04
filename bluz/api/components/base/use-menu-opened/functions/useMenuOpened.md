[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/use-menu-opened](../index.md) / useMenuOpened

# Function: useMenuOpened()

> **useMenuOpened**(`onOpen?`): \[`boolean`, (`event`) => `void`\]

Defined in: [ui/src/components/base/use-menu-opened.ts:16](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/base/use-menu-opened.ts#L16)

Whether a Select's menu has been opened yet, so its options can wait.

MUI's Select maps and clones every MenuItem child on each render, open or
not. A closed picker over the whole Hive catalogue (thousands of lessons)
spent most of the event dialog's open time building rows nobody could see.
Until the first open, render only the selected options — MUI reads the shown
value off them — and the full list from then on, so the rows stay put
through the menu's close animation and every later open.

## Parameters

### onOpen?

(`event`) => `void`

The caller's own `onOpen`, still called on every open.

## Returns

\[`boolean`, (`event`) => `void`\]

Whether the menu has opened, and the `onOpen` to hand the Select.
