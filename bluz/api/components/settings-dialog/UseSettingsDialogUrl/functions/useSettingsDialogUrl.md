[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/settings-dialog/UseSettingsDialogUrl](../index.md) / useSettingsDialogUrl

# Function: useSettingsDialogUrl()

> **useSettingsDialogUrl**(): `object`

Defined in: [ui/src/components/settings-dialog/UseSettingsDialogUrl.ts:31](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/UseSettingsDialogUrl.ts#L31)

## Returns

`object`

### activeTab

> **activeTab**: `"colors"` \| `"courses"` \| `"rooms"` \| `"outsiders"` \| `"iterations"` \| `"personal"` \| `"global"`

### closeDialog

> **closeDialog**: () => `void`

#### Returns

`void`

### isOpen

> **isOpen**: `boolean`

### openDialog

> **openDialog**: (`tab`, `edit?`) => `void`

#### Parameters

##### tab?

`"colors"` \| `"courses"` \| `"rooms"` \| `"outsiders"` \| `"iterations"` \| `"personal"` \| `"global"`

##### edit?

`Partial`\<`Record`\<`"editRoom"` \| `"editOutsider"`, `string`\>\>

#### Returns

`void`

### setTab

> **setTab**: (`tab`) => `void`

#### Parameters

##### tab

`"colors"` \| `"courses"` \| `"rooms"` \| `"outsiders"` \| `"iterations"` \| `"personal"` \| `"global"`

#### Returns

`void`
