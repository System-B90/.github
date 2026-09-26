[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/CalendarStoreMenu](../index.md) / StoreEntryAction

# Type Alias: StoreEntryAction\<TEntry\>

> **StoreEntryAction**\<`TEntry`\> = `object`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:17](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L17)

One icon action rendered on the trailing edge of a stored-entry row.

## Type Parameters

### TEntry

`TEntry`

## Properties

### color?

> `optional` **color?**: `"error"`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:20](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L20)

***

### icon

> **icon**: `ReactNode`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:19](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L19)

***

### onClick

> **onClick**: (`entry`, `close`) => `void`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:22](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L22)

`close` dismisses the popover — call it after a state-replacing action.

#### Parameters

##### entry

`TEntry`

##### close

() => `void`

#### Returns

`void`

***

### tooltip

> **tooltip**: `string`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:18](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L18)
