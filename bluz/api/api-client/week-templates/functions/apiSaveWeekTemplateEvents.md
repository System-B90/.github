[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/week-templates](../index.md) / apiSaveWeekTemplateEvents

# Function: apiSaveWeekTemplateEvents()

> **apiSaveWeekTemplateEvents**(`id`, `events`, `applyToCutWeeks`, `iterationId?`): `Promise`\<[`ApiWeekTemplateSaveResponse`](../../../api-shared/types/week-template/type-aliases/ApiWeekTemplateSaveResponse.md)\>

Defined in: [ui/src/api-client/week-templates.ts:88](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-client/week-templates.ts#L88)

Replaces a template's events with an edited week.

## Parameters

### id

`string`

### events

[`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]

### applyToCutWeeks

`boolean`

### iterationId?

`string`

## Returns

`Promise`\<[`ApiWeekTemplateSaveResponse`](../../../api-shared/types/week-template/type-aliases/ApiWeekTemplateSaveResponse.md)\>
