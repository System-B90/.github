[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/week-template](../index.md) / templateIdsByWeekStart

# Function: templateIdsByWeekStart()

> **templateIdsByWeekStart**(`events`): `Record`\<`string`, [`WeekTemplateId`](../type-aliases/WeekTemplateId.md)\>

Defined in: [ui/src/api-shared/types/week-template.ts:173](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/week-template.ts#L173)

The template each cut week was cut with, keyed by the week's Sunday, read
off the stamps on its cut events. Unstamped weeks are left out.

## Parameters

### events

`Pick`\<[`DbEventDocument`](../../event/type-aliases/DbEventDocument.md), `"ganttOccurrenceDate"` \| `"weekTemplateId"`\>[]

## Returns

`Record`\<`string`, [`WeekTemplateId`](../type-aliases/WeekTemplateId.md)\>
