[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/CalendarStoreMenu](../index.md) / CalendarStoreMenuProps

# Type Alias: CalendarStoreMenuProps\<TEntry\>

> **CalendarStoreMenuProps**\<`TEntry`\> = `object`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:25](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L25)

## Type Parameters

### TEntry

`TEntry` *extends* `object`

## Properties

### actions

> **actions**: [`StoreEntryAction`](StoreEntryAction.md)\<`TEntry`\>[]

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:57](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L57)

***

### busyId

> **busyId**: `null` \| `string`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:50](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L50)

Non-null while one entry is mutating; disables all row actions.

***

### children?

> `optional` **children?**: `ReactNode`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:59](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L59)

Extra nodes rendered next to the popover (e.g. confirmation dialogs).

***

### createIcon

> **createIcon**: `ReactNode`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:44](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L44)

Icon of the create button.

***

### createLabel

> **createLabel**: `string`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:42](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L42)

Label of the create button.

***

### disabled?

> `optional` **disabled?**: `boolean`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:34](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L34)

Disables the toolbar button and swaps its tooltip for `disabledTooltip`
("coming soon" placeholders). The popover never opens while set.

***

### disabledTooltip?

> `optional` **disabledTooltip?**: `string`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:36](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L36)

Tooltip shown instead of `tooltip` while `disabled` is set.

***

### emptyText

> **emptyText**: `string`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:46](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L46)

Text shown when the store holds no entries.

***

### entries

> **entries**: `TEntry`[]

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:47](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L47)

***

### icon

> **icon**: `ReactNode`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:29](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L29)

Icon inside the toolbar button.

***

### loading

> **loading**: `boolean`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:48](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L48)

***

### nameLabel

> **nameLabel**: `string`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:40](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L40)

Label of the "new entry name" text field.

***

### onCreate

> **onCreate**: (`label`) => `Promise`\<`void`\> \| `void`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:54](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L54)

Create a new entry from the current calendar under the given name.

#### Parameters

##### label

`string`

#### Returns

`Promise`\<`void`\> \| `void`

***

### onRefresh

> **onRefresh**: () => `Promise`\<`void`\> \| `void`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:52](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L52)

Fetch the entry list. Called whenever the popover opens.

#### Returns

`Promise`\<`void`\> \| `void`

***

### renderEntry

> **renderEntry**: (`entry`) => `object`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:56](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L56)

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

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:38](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L38)

Popover heading.

***

### tooltip

> **tooltip**: `string`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:27](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L27)

Tooltip on the toolbar button.
