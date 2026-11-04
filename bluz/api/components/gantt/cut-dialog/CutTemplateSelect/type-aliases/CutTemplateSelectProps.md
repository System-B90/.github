[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/cut-dialog/CutTemplateSelect](../index.md) / CutTemplateSelectProps

# Type Alias: CutTemplateSelectProps

> **CutTemplateSelectProps** = `object`

Defined in: [ui/src/components/gantt/cut-dialog/CutTemplateSelect.tsx:6](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/gantt/cut-dialog/CutTemplateSelect.tsx#L6)

## Properties

### emptyLabel?

> `optional` **emptyLabel?**: `string`

Defined in: [ui/src/components/gantt/cut-dialog/CutTemplateSelect.tsx:15](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/gantt/cut-dialog/CutTemplateSelect.tsx#L15)

What `""` means, when not "the default template": the reload keeps
each week's own template. The default is then listed by name.

***

### onChange

> **onChange**: (`templateId`) => `void`

Defined in: [ui/src/components/gantt/cut-dialog/CutTemplateSelect.tsx:10](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/gantt/cut-dialog/CutTemplateSelect.tsx#L10)

#### Parameters

##### templateId

`string`

#### Returns

`void`

***

### templates

> **templates**: [`WeekTemplate`](../../../../../api-shared/types/week-template/type-aliases/WeekTemplate.md)[]

Defined in: [ui/src/components/gantt/cut-dialog/CutTemplateSelect.tsx:7](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/gantt/cut-dialog/CutTemplateSelect.tsx#L7)

***

### value

> **value**: `string`

Defined in: [ui/src/components/gantt/cut-dialog/CutTemplateSelect.tsx:9](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/gantt/cut-dialog/CutTemplateSelect.tsx#L9)

Selected template id; `""` ⇒ the default template, or `emptyLabel`.
