[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/settings-dialog/tabs/global/common](../index.md) / SettingsTabProps

# Type Alias: SettingsTabProps\<TEntity, FormCardProps, ListCardProps\>

> **SettingsTabProps**\<`TEntity`, `FormCardProps`, `ListCardProps`\> = `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/index.tsx:35](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/settings-dialog/tabs/global/common/index.tsx#L35)

## Type Parameters

### TEntity

`TEntity`

### FormCardProps

`FormCardProps` *extends* `Omit`\<[`FormCardBaseProps`](../FormCard/type-aliases/FormCardBaseProps.md)\<`TEntity`\>, `"selectedEntity"`\>

### ListCardProps

`ListCardProps` *extends* `Omit`\<[`ReadOnlyListCardBaseProps`](ReadOnlyListCardBaseProps.md)\<`TEntity`\>, `"selectedEntity"`\> = `Omit`\<[`ListCardBaseProps`](ListCardBaseProps.md)\<`TEntity`\>, `"selectedEntity"`\>

## Properties

### FormCard

> **FormCard**: [`FormCard`](FormCard.md)\<`TEntity`, `FormCardProps`\>

Defined in: [ui/src/components/settings-dialog/tabs/global/common/index.tsx:41](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/settings-dialog/tabs/global/common/index.tsx#L41)

***

### formCardProps

> **formCardProps**: `FormCardProps`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/index.tsx:44](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/settings-dialog/tabs/global/common/index.tsx#L44)

***

### ListCard

> **ListCard**: [`ListCard`](ListCard.md)\<`TEntity`, `ListCardProps`\>

Defined in: [ui/src/components/settings-dialog/tabs/global/common/index.tsx:40](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/settings-dialog/tabs/global/common/index.tsx#L40)

***

### listCardProps

> **listCardProps**: `ListCardProps`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/index.tsx:43](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/settings-dialog/tabs/global/common/index.tsx#L43)

***

### selectedEntity

> **selectedEntity**: `null` \| `TEntity`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/index.tsx:42](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/settings-dialog/tabs/global/common/index.tsx#L42)
