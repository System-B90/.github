[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/api-layer](../index.md) / ApiT

# Type Alias: ApiT\<T\>

> **ApiT**\<`T`\> = `T` *extends* [`GanttCurriculum`](../../models/curriculum/type-aliases/GanttCurriculum.md) ? [`ApiCurriculum`](ApiCurriculum.md) : `T` *extends* [`GanttSyllabus`](../../models/syllabus/type-aliases/GanttSyllabus.md) ? [`ApiSyllabus`](ApiSyllabus.md) : `T` *extends* [`GanttModule`](../../models/module/type-aliases/GanttModule.md) ? [`ApiModule`](ApiModule.md) : `T` *extends* [`GanttEvent`](../../models/event/type-aliases/GanttEvent.md) ? [`ApiModuleEvent`](ApiModuleEvent.md) : `T` *extends* [`GanttWeek`](../../models/week/type-aliases/GanttWeek.md) ? [`ApiCurriculumWeek`](ApiCurriculumWeek.md) : `T` *extends* [`GanttDay`](../../models/day/type-aliases/GanttDay.md) ? [`ApiCurriculumDay`](ApiCurriculumDay.md) : `never`

Defined in: [ui/src/api-shared/types/gantt/api-layer.ts:106](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/api-layer.ts#L106)

## Type Parameters

### T

`T`
