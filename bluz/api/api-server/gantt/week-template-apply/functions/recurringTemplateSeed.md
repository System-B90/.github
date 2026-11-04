[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/week-template-apply](../index.md) / recurringTemplateSeed

# Function: recurringTemplateSeed()

> **recurringTemplateSeed**(): `Promise`\<[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]\>

Defined in: [ui/src/api-server/gantt/week-template-apply.ts:101](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/week-template-apply.ts#L101)

A new template's starting point: one parked copy of each recurring event of
the curriculum linked to the current iteration, named and coursed exactly
as the cut would write it, minus shuffles (templates ignore them). Empty
when nothing is linked.

## Returns

`Promise`\<[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]\>
