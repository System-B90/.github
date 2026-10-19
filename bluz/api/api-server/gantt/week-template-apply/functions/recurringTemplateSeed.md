[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/week-template-apply](../index.md) / recurringTemplateSeed

# Function: recurringTemplateSeed()

> **recurringTemplateSeed**(): `Promise`\<[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]\>

Defined in: [ui/src/api-server/gantt/week-template-apply.ts:122](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/gantt/week-template-apply.ts#L122)

A new template's starting point: one parked copy of each recurring event of
the curriculum linked to the current iteration, named and coursed exactly
as the cut would write it, minus shuffles (templates ignore them). Empty
when nothing is linked.

## Returns

`Promise`\<[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]\>
