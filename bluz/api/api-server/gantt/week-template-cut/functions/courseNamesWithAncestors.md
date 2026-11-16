[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/week-template-cut](../index.md) / courseNamesWithAncestors

# Function: courseNamesWithAncestors()

> **courseNamesWithAncestors**(`courseIds`, `courses`): `string`[]

Defined in: [ui/src/api-server/gantt/week-template-cut.ts:100](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/api-server/gantt/week-template-cut.ts#L100)

Names of the courses an event's course ids stand for, plus every ancestor.
Templates ignore shuffles, so a template event for "Apollo" must still match
a cut event that landed on one of Apollo's shuffles.

## Parameters

### courseIds

`Iterable`\<`string`\>

### courses

[`Course`](../../../../api-shared/types/course/type-aliases/Course.md)[]

## Returns

`string`[]
