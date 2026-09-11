[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/common/FormHeader](../index.md) / SettingsFormHeaderProps

# Type Alias: SettingsFormHeaderProps

> **SettingsFormHeaderProps** = `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/FormHeader.tsx:13](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/FormHeader.tsx#L13)

The header every settings edit panel shows: an edit badge that turns
secondary while creating, a title, and a subtitle that also covers the
"nothing selected yet" state. Each tab used to spell this ternary out itself,
which is how their wording and colours drifted apart — passing the three
strings instead keeps the shape identical across tabs.

## Properties

### action?

> `optional` **action?**: `ReactNode`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/FormHeader.tsx:21](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/FormHeader.tsx#L21)

Optional trailing control, e.g. the outsider QR button.

***

### icon?

> `optional` **icon?**: `React.ElementType`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/FormHeader.tsx:15](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/FormHeader.tsx#L15)

Defaults to the edit pencil; only override when a tab needs its own.

***

### isCreating

> **isCreating**: `boolean`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/FormHeader.tsx:16](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/FormHeader.tsx#L16)

***

### isEditing

> **isEditing**: `boolean`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/FormHeader.tsx:17](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/FormHeader.tsx#L17)

***

### subtitles

> **subtitles**: `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/FormHeader.tsx:19](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/FormHeader.tsx#L19)

#### creating

> **creating**: `string`

#### editing

> **editing**: `string`

#### empty

> **empty**: `string`

***

### titles

> **titles**: `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/FormHeader.tsx:18](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/FormHeader.tsx#L18)

#### creating

> **creating**: `string`

#### editing

> **editing**: `string`
