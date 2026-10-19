[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/week-templates](../index.md) / apiSaveWeekTemplateEvents

# Function: apiSaveWeekTemplateEvents()

> **apiSaveWeekTemplateEvents**(`id`, `events`, `applyToCutWeeks`, `iterationId?`): `Promise`\<[`ApiWeekTemplateSaveResponse`](../../../api-shared/types/week-template/type-aliases/ApiWeekTemplateSaveResponse.md)\>

Defined in: [ui/src/api-client/week-templates.ts:79](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-client/week-templates.ts#L79)

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
