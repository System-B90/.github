[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/week-templates](../index.md) / apiSaveWeekTemplateEvents

# Function: apiSaveWeekTemplateEvents()

> **apiSaveWeekTemplateEvents**(`id`, `events`, `applyToCutWeeks`, `iterationId?`): `Promise`\<[`ApiWeekTemplateSaveResponse`](../../../api-shared/types/week-template/type-aliases/ApiWeekTemplateSaveResponse.md)\>

Defined in: [ui/src/api-client/week-templates.ts:79](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-client/week-templates.ts#L79)

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
