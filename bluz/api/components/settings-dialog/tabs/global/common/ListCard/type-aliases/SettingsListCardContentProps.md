[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/common/ListCard](../index.md) / SettingsListCardContentProps

# Type Alias: SettingsListCardContentProps

> **SettingsListCardContentProps** = `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx:34](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx#L34)

## Properties

### addButtonLabel

> **addButtonLabel**: [`SettingsAddButtonProps`](../../AddButton/type-aliases/SettingsAddButtonProps.md)\[`"label"`\]

Defined in: [ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx:47](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx#L47)

***

### handleStartCreate

> **handleStartCreate**: () => `void`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx:46](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx#L46)

#### Returns

`void`

***

### headerProps

> **headerProps**: [`SettingsSectionHeaderProps`](../../SectionHeader/type-aliases/SettingsSectionHeaderProps.md)

Defined in: [ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx:42](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx#L42)

***

### isLoading?

> `optional` **isLoading?**: `boolean`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx:41](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx#L41)

While true the list shows skeleton rows. Without it an in-flight fetch
is indistinguishable from an empty collection, and the tab flashes
"no entries" before the data lands.

***

### items

> **items**: `ReactNode`[]

Defined in: [ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx:35](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx#L35)

***

### searchMessages

> **searchMessages**: `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx:48](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx#L48)

#### noEntries

> **noEntries**: `string`

#### noMatches

> **noMatches**: `string`

***

### searchPlaceholder

> **searchPlaceholder**: [`SettingsSearchFieldProps`](../../SearchField/type-aliases/SettingsSearchFieldProps.md)\[`"placeholder"`\]

Defined in: [ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx:43](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx#L43)

***

### searchQuery

> **searchQuery**: `string`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx:44](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx#L44)

***

### setSearchQuery

> **setSearchQuery**: (`query`) => `void`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx:45](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/ListCard.tsx#L45)

#### Parameters

##### query

`string`

#### Returns

`void`
