[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/default-expansion](../index.md) / defaultExpandedSyllabusIds

# Function: defaultExpandedSyllabusIds()

> **defaultExpandedSyllabusIds**(`syllabusIds`, `state`, `courses`, `userId`): `string`[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/default-expansion.ts:26](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/default-expansion.ts#L26)

The syllabuses a viewer sees open before touching anything: the ones they
orchestrate; failing that, the ones that exist for a course they are in
(a syllabus with no course is for everyone); failing that, none.

## Parameters

### syllabusIds

`string`[]

### state

`State`

### courses

[`Course`](../../../../../../../../api-shared/types/course/type-aliases/Course.md)[]

### userId

`number` \| `null` \| `undefined`

## Returns

`string`[]
