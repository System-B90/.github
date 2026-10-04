[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/Submenu](../index.md) / PickerSubmenuProps

# Type Alias: PickerSubmenuProps

> **PickerSubmenuProps** = `object` & `Omit`\<`MenuItemProps`, `"children"` \| `"onClick"`\>

Defined in: [ui/src/components/schedule/event-context-menu/Submenu.tsx:96](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/schedule/event-context-menu/Submenu.tsx#L96)

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
