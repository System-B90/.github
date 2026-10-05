[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / buildStudentPaths

# Function: buildStudentPaths()

> **buildStudentPaths**(`courses`, `assignedCourseIds`, `includeRoots`): [`StudentPath`](../type-aliases/StudentPath.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:118](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/student-load.ts#L118)

The student paths a curriculum's syllabuses and events distinguish: every
root-to-leaf chain of the course tree, cut at the deepest course anything
is assigned to. A course's students are split between all of its
sub-courses, so once one sub-course matters its siblings are paths too.
Shuffle courses are not paths — shuffles live inside a syllabus. Without
any course, there is a single all-students path.

## Parameters

### courses

`Pick`\<[`Course`](../../../../../api-shared/types/course/type-aliases/Course.md), `"name"` \| `"id"` \| `"description"` \| `"parentId"`\>[]

### assignedCourseIds

`Iterable`\<`string`\>

### includeRoots

`boolean`

Something is assigned to no course, i.e. to the root.

## Returns

[`StudentPath`](../type-aliases/StudentPath.md)[]
