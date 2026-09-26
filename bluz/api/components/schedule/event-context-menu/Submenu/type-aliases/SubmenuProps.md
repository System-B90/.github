[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/Submenu](../index.md) / SubmenuProps

# Type Alias: SubmenuProps

> **SubmenuProps** = `object` & `Omit`\<`MenuItemProps`, `"children"` \| `"onClick"`\>

Defined in: [ui/src/components/schedule/event-context-menu/Submenu.tsx:44](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/Submenu.tsx#L44)

Anything the parent `MenuList` injects into what it believes is a plain
menu item — `ref`, `tabIndex`, `autoFocus` — plus the submenu's own props.
Forwarding the injected set is what keeps the entry reachable by keyboard:
MenuList focuses items through the ref it hands down, and a component that
swallows it drops out of the arrow-key walk entirely.

## Type Declaration

### children

> **children**: `ReactNode`

Rendered inside the nested menu.

### icon

> **icon**: `ReactNode`

### label

> **label**: `string`
