[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/syllabus-shuffles](../index.md) / shuffleCoursesForEvents

# Function: shuffleCoursesForEvents()

> **shuffleCoursesForEvents**(`events`, `curriculum`, `courses`): [`Course`](../../../../../api-shared/types/course/type-aliases/Course.md)[]

Defined in: [ui/src/components/schedule/event-context-menu/syllabus-shuffles.ts:36](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/event-context-menu/syllabus-shuffles.ts#L36)

Shuffle courses on offer for `events`: their syllabuses' shuffles, in
syllabus order, plus any shuffle already assigned so it can be removed.

## Parameters

### events

readonly `Pick`\<[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md), `"subject"` \| `"courses"` \| `"ganttEventId"`\>[]

### curriculum

`Pick`\<[`ApiCurriculum`](../../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md), `"c2s"`\> \| `null`

### courses

readonly [`Course`](../../../../../api-shared/types/course/type-aliases/Course.md)[]

## Returns

[`Course`](../../../../../api-shared/types/course/type-aliases/Course.md)[]
