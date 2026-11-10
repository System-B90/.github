[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/week-templates/use-load-template](../index.md) / useTemplateUrl

# Function: useTemplateUrl()

> **useTemplateUrl**(): `void`

Defined in: [ui/src/components/week-templates/use-load-template.ts:81](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/week-templates/use-load-template.ts#L81)

Every template has its own editing URL, `/?template=<id>`. Opening that URL
opens the template once the first fetch lands. While a template is open,
however it was opened, the address bar names it, so the link can be shared
and a refresh reopens it. Ending the session drops the param. Edits are
local until saved, so leaving or refreshing with unsaved edits asks first.

## Returns

`void`
