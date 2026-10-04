[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/ImportExportMenuButton](../index.md) / ImportExportMenuButtonProps

# Type Alias: ImportExportMenuButtonProps

> **ImportExportMenuButtonProps** = `object`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:18](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L18)

## Properties

### accept?

> `optional` **accept?**: `string`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:24](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L24)

***

### color?

> `optional` **color?**: `ButtonProps`\[`"color"`\]

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:27](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L27)

***

### command?

> `optional` **command?**: `object`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:42](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L42)

Mirror the menu's items in the command palette as `<id>.export`,
`<id>.export.excel` and `<id>.import`, under `group`.

#### group

> **group**: `string`

#### id

> **id**: `string`

#### keywords?

> `optional` **keywords?**: `string`[]

***

### exportDisabled?

> `optional` **exportDisabled?**: `boolean`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:28](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L28)

***

### exportExcelLabel?

> `optional` **exportExcelLabel?**: `string`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:37](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L37)

***

### exportFilenamePrefix?

> `optional` **exportFilenamePrefix?**: `string`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:32](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L32)

***

### exportLabel?

> `optional` **exportLabel?**: `string`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:22](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L22)

***

### exportTitle?

> `optional` **exportTitle?**: `string`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:33](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L33)

***

### iconOnly?

> `optional` **iconOnly?**: `boolean`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:30](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L30)

***

### importDisabled?

> `optional` **importDisabled?**: `boolean`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:29](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L29)

***

### importLabel?

> `optional` **importLabel?**: `string`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:21](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L21)

***

### loading?

> `optional` **loading?**: `boolean`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:31](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L31)

***

### onExport

> **onExport**: () => `Promise`\<`unknown`\> \| `unknown`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:19](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L19)

#### Returns

`Promise`\<`unknown`\> \| `unknown`

***

### onExportError?

> `optional` **onExportError?**: (`error`) => `void`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:35](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L35)

#### Parameters

##### error

`unknown`

#### Returns

`void`

***

### onExportExcel?

> `optional` **onExportExcel?**: () => `Promise`\<`void`\> \| `void`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:36](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L36)

#### Returns

`Promise`\<`void`\> \| `void`

***

### onExportSuccess?

> `optional` **onExportSuccess?**: () => `void`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:34](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L34)

#### Returns

`void`

***

### onImport

> **onImport**: (`e`) => `void`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:20](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L20)

#### Parameters

##### e

`React.ChangeEvent`\<`HTMLInputElement`\>

#### Returns

`void`

***

### size?

> `optional` **size?**: `ButtonProps`\[`"size"`\]

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:25](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L25)

***

### triggerLabel?

> `optional` **triggerLabel?**: `string`

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:23](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L23)

***

### variant?

> `optional` **variant?**: `ButtonProps`\[`"variant"`\]

Defined in: [ui/src/components/base/ImportExportMenuButton.tsx:26](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/ImportExportMenuButton.tsx#L26)
