[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/syllabus-shuffles](../index.md) / shuffleCoursesForEvents

# Function: shuffleCoursesForEvents()

> **shuffleCoursesForEvents**(`events`, `curriculum`, `courses`): [`Course`](../../../../../api-shared/types/course/type-aliases/Course.md)[]

Defined in: [ui/src/components/schedule/event-context-menu/syllabus-shuffles.ts:36](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/schedule/event-context-menu/syllabus-shuffles.ts#L36)

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
