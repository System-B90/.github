[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/CalendarStoreMenu](../index.md) / StoreEntryAction

# Type Alias: StoreEntryAction\<TEntry\>

> **StoreEntryAction**\<`TEntry`\> = `object`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:22](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L22)

One icon action rendered on the trailing edge of a stored-entry row.

## Type Parameters

### TEntry

`TEntry`

## Properties

### color?

> `optional` **color?**: `"error"`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:25](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L25)

***

### confirm?

> `optional` **confirm?**: `object`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:30](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L30)

Asks before running — required for anything that cannot be undone,
e.g. deleting a stored entry (docs/ux-guidelines.md §5.7).

#### confirmLabel

> **confirmLabel**: `string`

#### message

> **message**: (`entry`) => `string`

##### Parameters

###### entry

`TEntry`

##### Returns

`string`

#### title

> **title**: `string`

***

### disabled?

> `optional` **disabled?**: (`entry`) => `boolean`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:36](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L36)

Disables the action on rows it does not apply to.

#### Parameters

##### entry

`TEntry`

#### Returns

`boolean`

***

### icon

> **icon**: `ReactNode`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:24](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L24)

***

### onClick

> **onClick**: (`entry`, `close`) => `void`

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:38](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L38)

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

Defined in: [ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx:23](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/schedule/calendar/calendar/CalendarStoreMenu.tsx#L23)
