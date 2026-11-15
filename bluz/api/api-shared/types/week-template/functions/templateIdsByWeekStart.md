[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/week-template](../index.md) / templateIdsByWeekStart

# Function: templateIdsByWeekStart()

> **templateIdsByWeekStart**(`events`): `Record`\<`string`, [`WeekTemplateId`](../type-aliases/WeekTemplateId.md)\>

Defined in: [ui/src/api-shared/types/week-template.ts:209](https://github.com/System-B90/Bluz/blob/ef5f1592ad9f013b150ea581b494f4fff71a8490/ui/src/api-shared/types/week-template.ts#L209)

The template each cut week was cut with, keyed by the week's Sunday, read
off the stamps on its cut events. Unstamped weeks are left out.

## Parameters

### events

`Pick`\<[`DbEventDocument`](../../event/type-aliases/DbEventDocument.md), `"ganttOccurrenceDate"` \| `"weekTemplateId"`\>[]

## Returns

`Record`\<`string`, [`WeekTemplateId`](../type-aliases/WeekTemplateId.md)\>
