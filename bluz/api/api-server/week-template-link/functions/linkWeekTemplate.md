[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/week-template-link](../index.md) / linkWeekTemplate

# Function: linkWeekTemplate()

> **linkWeekTemplate**(`date`, `templateId`, `controller`): `Promise`\<\{ `link`: [`WeekTemplateLink`](../../../api-shared/types/week-template/type-aliases/WeekTemplateLink.md); `updatedEvents`: `number`; \}\>

Defined in: [ui/src/api-server/week-template-link.ts:80](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/week-template-link.ts#L80)

Link the week holding `date` to `templateId` without re-cutting it: every
live cut event of the week is restamped, so its prayer tint and its next
reload follow the new template. Event times are left alone, and so is
`updatedAt`: a stamp is metadata, not an edit (same as a reload's restamp).

## Parameters

### date

`string`

### templateId

`string`

### controller

[`DatabaseController`](../../mongo-db-controller/classes/DatabaseController.md)

## Returns

`Promise`\<\{ `link`: [`WeekTemplateLink`](../../../api-shared/types/week-template/type-aliases/WeekTemplateLink.md); `updatedEvents`: `number`; \}\>
