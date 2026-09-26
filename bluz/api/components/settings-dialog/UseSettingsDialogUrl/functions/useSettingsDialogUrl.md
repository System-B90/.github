[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/settings-dialog/UseSettingsDialogUrl](../index.md) / useSettingsDialogUrl

# Function: useSettingsDialogUrl()

> **useSettingsDialogUrl**(): `object`

Defined in: [ui/src/components/settings-dialog/UseSettingsDialogUrl.ts:31](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/settings-dialog/UseSettingsDialogUrl.ts#L31)

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
