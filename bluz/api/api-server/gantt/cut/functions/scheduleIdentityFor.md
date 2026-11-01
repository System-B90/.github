[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / scheduleIdentityFor

# Function: scheduleIdentityFor()

> **scheduleIdentityFor**(`ganttEvent`, `moduleHiveIds`, `hiveModuleSubjectById`, `naming?`): `object`

Defined in: [ui/src/api-server/gantt/cut.ts:610](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/gantt/cut.ts#L610)

The Hive linkage and schedule name a gantt event is cut with. Shared by the
cut itself and week-template matching (#997), which must see exactly the
name the cut will write.

## Parameters

### ganttEvent

[`ApiModuleEvent`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiModuleEvent.md)

### moduleHiveIds

`number`[]

### hiveModuleSubjectById

`Map`\<`number`, `number`\>

### naming?

#### syllabus

[`SyllabusNaming`](../type-aliases/SyllabusNaming.md) \| `undefined`

#### symbolBySubjectId

`Map`\<`number`, `string`\>

## Returns

`object`

### hiveModuleId

> **hiveModuleId**: `number` \| `null`

### hiveSubjectId

> **hiveSubjectId**: `number` \| `null`

### name

> **name**: `string`
