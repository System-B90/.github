[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/CalendarStoreMenu](../index.md) / CalendarStoreMenuProps

# Type Alias: CalendarStoreMenuProps\<TEntry\>

> **CalendarStoreMenuProps**\<`TEntry`\> = `object`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:41](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L41)

## Type Parameters

### TEntry

`TEntry` *extends* `object`

## Properties

### actions

> **actions**: [`StoreEntryAction`](StoreEntryAction.md)\<`TEntry`\>[]

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:73](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L73)

***

### active?

> `optional` **active?**: `boolean`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:79](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L79)

Marks the toolbar button as "something of mine is open".

***

### busyId

> **busyId**: `null` \| `string`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:66](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L66)

Non-null while one entry is mutating; disables all row actions.

***

### buttonRef?

> `optional` **buttonRef?**: `Ref`\<`HTMLButtonElement`\>

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:81](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L81)

Ref to the toolbar button — how an owner lets a tour spotlight it.

***

### children?

> `optional` **children?**: `ReactNode`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:75](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L75)

Extra nodes rendered next to the popover (e.g. confirmation dialogs).

***

### createIcon

> **createIcon**: `ReactNode`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:60](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L60)

Icon of the create button.

***

### createLabel

> **createLabel**: `string`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:58](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L58)

Label of the create button.

***

### disabled?

> `optional` **disabled?**: `boolean`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:50](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L50)

Disables the toolbar button and swaps its tooltip for `disabledTooltip`
("coming soon" placeholders). The popover never opens while set.

***

### disabledTooltip?

> `optional` **disabledTooltip?**: `string`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:52](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L52)

Tooltip shown instead of `tooltip` while `disabled` is set.

***

### emptyText

> **emptyText**: `string`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:62](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L62)

Text shown when the store holds no entries.

***

### entries

> **entries**: `TEntry`[]

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:63](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L63)

***

### header?

> `optional` **header?**: (`close`) => `ReactNode`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:77](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L77)

Rendered above the create field, e.g. the entry currently open.

#### Parameters

##### close

() => `void`

#### Returns

`ReactNode`

***

### icon

> **icon**: `ReactNode`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:45](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L45)

Icon inside the toolbar button.

***

### loading

> **loading**: `boolean`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:64](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L64)

***

### nameLabel

> **nameLabel**: `string`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:56](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L56)

Label of the "new entry name" text field.

***

### onCreate

> **onCreate**: (`label`) => `Promise`\<`void`\> \| `void`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:70](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L70)

Create a new entry from the current calendar under the given name.

#### Parameters

##### label

`string`

#### Returns

`Promise`\<`void`\> \| `void`

***

### onRefresh

> **onRefresh**: () => `Promise`\<`void`\> \| `void`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:68](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L68)

Fetch the entry list. Called whenever the popover opens.

#### Returns

`Promise`\<`void`\> \| `void`

***

### renderEntry

> **renderEntry**: (`entry`) => `object`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:72](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L72)

Primary and secondary text for one row.

#### Parameters

##### entry

`TEntry`

#### Returns

`object`

##### primary

> **primary**: `string`

##### secondary

> **secondary**: `string`

***

### title

> **title**: `string`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:54](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L54)

Popover heading.

***

### tooltip

> **tooltip**: `string`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:43](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L43)

Tooltip on the toolbar button.
