[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/week-templates/use-load-template](../index.md) / useTemplateUrl

# Function: useTemplateUrl()

> **useTemplateUrl**(): `void`

Defined in: [ui/src/components/week-templates/use-load-template.ts:81](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/week-templates/use-load-template.ts#L81)

Every template has its own editing URL, `/?template=<id>`. Opening that URL
opens the template once the first fetch lands. While a template is open,
however it was opened, the address bar names it, so the link can be shared
and a refresh reopens it. Ending the session drops the param. Edits are
local until saved, so leaving or refreshing with unsaved edits asks first.

## Returns

`void`
