[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/week-templates](../index.md) / apiSaveWeekTemplateEvents

# Function: apiSaveWeekTemplateEvents()

> **apiSaveWeekTemplateEvents**(`id`, `events`, `applyToCutWeeks`, `iterationId?`): `Promise`\<[`ApiWeekTemplateSaveResponse`](../../../api-shared/types/week-template/type-aliases/ApiWeekTemplateSaveResponse.md)\>

Defined in: [ui/src/api-client/week-templates.ts:88](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-client/week-templates.ts#L88)

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
