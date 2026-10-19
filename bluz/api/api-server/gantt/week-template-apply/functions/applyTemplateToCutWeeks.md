[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/week-template-apply](../index.md) / applyTemplateToCutWeeks

# Function: applyTemplateToCutWeeks()

> **applyTemplateToCutWeeks**(`template`): `Promise`\<[`ApiWeekTemplateApplyResult`](../../../../api-shared/types/week-template/type-aliases/ApiWeekTemplateApplyResult.md)\>

Defined in: [ui/src/api-server/gantt/week-template-apply.ts:85](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/week-template-apply.ts#L85)

Re-plan every week of the current iteration that was cut with `template`.
This is a gantt reload limited to those weeks, so events a person edited
since the cut are skipped, never overwritten, and every open schedule gets
the change live. Their prayer events are retimed too.

## Parameters

### template

[`WeekTemplate`](../../../../api-shared/types/week-template/type-aliases/WeekTemplate.md)

## Returns

`Promise`\<[`ApiWeekTemplateApplyResult`](../../../../api-shared/types/week-template/type-aliases/ApiWeekTemplateApplyResult.md)\>
