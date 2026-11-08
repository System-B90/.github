[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/week-template-link](../index.md) / resolveWeekTemplate

# Function: resolveWeekTemplate()

> **resolveWeekTemplate**(`date`, `controller`): `Promise`\<\{ `link`: [`WeekTemplateLink`](../../../api-shared/types/week-template/type-aliases/WeekTemplateLink.md); `template`: [`WeekTemplate`](../../../api-shared/types/week-template/type-aliases/WeekTemplate.md) \| `null`; \}\>

Defined in: [ui/src/api-server/week-template-link.ts:46](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/week-template-link.ts#L46)

The template the week holding `date` is linked to, with the link itself. A
week never cut, cut before templates existed, or stamped with a deleted
template gets the default, as a cut of it would.

## Parameters

### date

`string`

### controller

[`DatabaseController`](../../mongo-db-controller/classes/DatabaseController.md)

## Returns

`Promise`\<\{ `link`: [`WeekTemplateLink`](../../../api-shared/types/week-template/type-aliases/WeekTemplateLink.md); `template`: [`WeekTemplate`](../../../api-shared/types/week-template/type-aliases/WeekTemplate.md) \| `null`; \}\>
