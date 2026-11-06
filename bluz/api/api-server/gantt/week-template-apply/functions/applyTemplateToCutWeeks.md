[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/week-template-apply](../index.md) / applyTemplateToCutWeeks

# Function: applyTemplateToCutWeeks()

> **applyTemplateToCutWeeks**(`template`): `Promise`\<[`ApiWeekTemplateApplyResult`](../../../../api-shared/types/week-template/type-aliases/ApiWeekTemplateApplyResult.md)\>

Defined in: [ui/src/api-server/gantt/week-template-apply.ts:74](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/gantt/week-template-apply.ts#L74)

Re-plan every week of the current iteration that was cut with `template`.
This is a gantt reload limited to those weeks, so events a person edited
since the cut are skipped, never overwritten, and every open schedule gets
the change live. The prayer tint reads the template's times itself.

## Parameters

### template

[`WeekTemplate`](../../../../api-shared/types/week-template/type-aliases/WeekTemplate.md)

## Returns

`Promise`\<[`ApiWeekTemplateApplyResult`](../../../../api-shared/types/week-template/type-aliases/ApiWeekTemplateApplyResult.md)\>
