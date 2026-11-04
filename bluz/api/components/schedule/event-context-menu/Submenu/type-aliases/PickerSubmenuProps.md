[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/Submenu](../index.md) / PickerSubmenuProps

# Type Alias: PickerSubmenuProps

> **PickerSubmenuProps** = `object` & `Omit`\<`MenuItemProps`, `"children"` \| `"onClick"`\>

Defined in: [ui/src/components/schedule/event-context-menu/Submenu.tsx:97](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/schedule/event-context-menu/Submenu.tsx#L97)

## Type Declaration

### clearLabel?

> `optional` **clearLabel?**: `string`

Entry that unassigns instead of picking. Omitted when not meaningful.

### emptyLabel?

> `optional` **emptyLabel?**: `string`

### icon

> **icon**: `ReactNode`

### label

> **label**: `string`

### onPick

> **onPick**: (`id`) => `void`

#### Parameters

##### id

`null` \| `string`

#### Returns

`void`

### options

> **options**: `ReadonlyArray`\<[`PickerOption`](PickerOption.md)\>
