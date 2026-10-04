[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/fixture](../index.md) / FIXTURE\_EXECUTION

# Variable: FIXTURE\_EXECUTION

> `const` **FIXTURE\_EXECUTION**: `object`

Defined in: [ui/src/api-server/ai/benchmark/fixture.ts:335](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/ai/benchmark/fixture.ts#L335)

The planned-vs-actual gap the benchmark expects the model to notice: the
networking module is planned for 8 hours and only 3 are on the schedule.

## Type Declaration

### curriculumId

> **curriculumId**: `string` = `FIXTURE_CURRICULUM_ID`

### events

> **events**: `object`

#### events.fx-mod-1

> **fx-mod-1**: `object`

#### events.fx-mod-1.actual

> **actual**: `number` = `12`

#### events.fx-mod-1.planned

> **planned**: `number` = `12`

#### events.fx-mod-1.title

> **title**: `string` = `"מתמטיקה בדידה"`

#### events.fx-mod-2

> **fx-mod-2**: `object`

#### events.fx-mod-2.actual

> **actual**: `number` = `3`

#### events.fx-mod-2.planned

> **planned**: `number` = `8`

#### events.fx-mod-2.title

> **title**: `string` = `"רשתות"`
