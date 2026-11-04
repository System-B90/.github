[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/week-templates/use-load-template](../index.md) / useLoadTemplate

# Function: useLoadTemplate()

> **useLoadTemplate**(): (`templateId`) => `Promise`\<\{ `eventCount`: `number`; `name`: `string`; \}\>

Defined in: [ui/src/components/week-templates/use-load-template.ts:24](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/week-templates/use-load-template.ts#L24)

Opens a week template for editing (#997). Editing a template is offline by
nature: its events replace the shown week, every edit stays local, and
leaving offline mode offers to save the week back into the template.

## Returns

Loads the template into the shown week; resolves to its name.

(`templateId`) => `Promise`\<\{ `eventCount`: `number`; `name`: `string`; \}\>
