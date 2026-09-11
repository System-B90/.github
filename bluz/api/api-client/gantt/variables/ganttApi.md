[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/gantt](../index.md) / ganttApi

# Variable: ganttApi

> `const` **ganttApi**: `object`

Defined in: [ui/src/api-client/gantt/index.ts:18](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/index.ts#L18)

## Type Declaration

### applyShuffles

> `readonly` **applyShuffles**: (`syllabusId`, `shuffles`) => `Promise`\<[`ShuffleUsages`](../../../api-shared/types/gantt/shuffles/type-aliases/ShuffleUsages.md)\> = `apiApplyShuffles`

Replaces the syllabus' shuffle list, stripping every removed name off the
modules and events that carry it. Returns what was stripped.

#### Parameters

##### syllabusId

`string`

##### shuffles

`string`[]

#### Returns

`Promise`\<[`ShuffleUsages`](../../../api-shared/types/gantt/shuffles/type-aliases/ShuffleUsages.md)\>

### constraints

> `readonly` **constraints**: `object` = `ganttConstraintsApi`

#### constraints.apiCreate

> `readonly` **apiCreate**: (`curriculumId`, `payload`, `options?`) => `Promise`\<[`GanttConstraint`](../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)\> = `apiCreateConstraint`

POST: Creates a new relational or temporal constraint.
Note: Assumes the endpoint is nested under the curriculum for uniform routing.

##### Parameters

###### curriculumId

`string`

###### payload

[`CreateConstraintPayload`](../../../api-shared/types/gantt/create-payloads/type-aliases/CreateConstraintPayload.md)

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<[`GanttConstraint`](../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)\>

#### constraints.apiDelete

> `readonly` **apiDelete**: (`curriculumId`, `id`, `options?`) => `Promise`\<`void`\> = `apiDeleteConstraint`

DELETE: Removes a constraint.

##### Parameters

###### curriculumId

`string`

###### id

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`void`\>

#### constraints.apiGet

> `readonly` **apiGet**: (`curriculumId`, `__namedParameters`, `options?`) => `Promise`\<[`GanttConstraint`](../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]\> = `apiGetConstraints`

GET: Retrieves all constraints for a curriculum's modules and events.

##### Parameters

###### curriculumId

`string`

###### \_\_namedParameters

###### moduleId?

`string`

###### syllabusId?

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<[`GanttConstraint`](../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]\>

#### constraints.apiUpdate

> `readonly` **apiUpdate**: (`curriculumId`, `id`, `payload`, `options?`) => `Promise`\<[`GanttConstraint`](../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)\> = `apiUpdateConstraint`

PATCH: Updates an existing constraint.

##### Parameters

###### curriculumId

`string`

###### id

`string`

###### payload

`Partial`\<[`CreateConstraintPayload`](../../../api-shared/types/gantt/create-payloads/type-aliases/CreateConstraintPayload.md)\>

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<[`GanttConstraint`](../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)\>

### curriculum

> `readonly` **curriculum**: `object` = `curriculumApi`

#### curriculum.apiCreate

> `readonly` **apiCreate**: (`payload`, `options?`) => `Promise`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../base/type-aliases/BaseDocument.md)\>

##### Parameters

###### payload

`TCreatePayload`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../base/type-aliases/BaseDocument.md)\>

#### curriculum.apiDelete

> `readonly` **apiDelete**: (`id`, `options?`) => `Promise`\<`void`\>

##### Parameters

###### id

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`void`\>

#### curriculum.apiDuplicate

> **apiDuplicate**: (`id`, `overrides`, `options?`) => `Promise`\<[`GanttCurriculumDocument`](../curriculum/type-aliases/GanttCurriculumDocument.md)\>

Server-side deep clone of a curriculum into a fully independent copy (#319,
#322). Returns the freshly created curriculum.

##### Parameters

###### id

`string`

###### overrides?

[`DuplicateCurriculumOverrides`](../curriculum/type-aliases/DuplicateCurriculumOverrides.md) = `{}`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<[`GanttCurriculumDocument`](../curriculum/type-aliases/GanttCurriculumDocument.md)\>

#### curriculum.apiExport

> **apiExport**: (`id`, `options?`) => `Promise`\<[`GanttCurriculumExport`](../curriculum/type-aliases/GanttCurriculumExport.md)\>

##### Parameters

###### id

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<[`GanttCurriculumExport`](../curriculum/type-aliases/GanttCurriculumExport.md)\>

#### curriculum.apiGet

> `readonly` **apiGet**: (`id`, `options?`) => `Promise`\<[`ApiCurriculum`](../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md)\>

##### Parameters

###### id

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<[`ApiCurriculum`](../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md)\>

#### curriculum.apiGetAllocatedTime

> `readonly` **apiGetAllocatedTime**: (`itemId`, `containerId`, `options?`) => `Promise`\<`number`\>

##### Parameters

###### itemId

`string`

###### containerId

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`number`\>

#### curriculum.apiGetMany

> `readonly` **apiGetMany**: (`ids`, `options?`) => `Promise`\<`Record`\<`string`, `object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../base/type-aliases/BaseDocument.md)\>\>

##### Parameters

###### ids

`string`[]

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`Record`\<`string`, `object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../base/type-aliases/BaseDocument.md)\>\>

#### curriculum.apiImport

> **apiImport**: (`payload`, `options?`) => `Promise`\<[`GanttCurriculumDocument`](../curriculum/type-aliases/GanttCurriculumDocument.md)\>

##### Parameters

###### payload

`unknown`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<[`GanttCurriculumDocument`](../curriculum/type-aliases/GanttCurriculumDocument.md)\>

#### curriculum.apiLink

> `readonly` **apiLink**: (`itemId`, `newParentId`, `options?`) => `Promise`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../base/type-aliases/BaseDocument.md)\>

##### Parameters

###### itemId

`string`

###### newParentId

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../base/type-aliases/BaseDocument.md)\>

#### curriculum.apiList

> `readonly` **apiList**: (`options?`) => `Promise`\<`Record`\<`string`, `string`\>\>

##### Parameters

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`Record`\<`string`, `string`\>\>

#### curriculum.apiListWithParents

> `readonly` **apiListWithParents**: (`options?`) => `Promise`\<`Record`\<`string`, [`ListEntryWithParent`](../base/type-aliases/ListEntryWithParent.md)\<[`GanttCurriculum`](../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculum.md)\>\>\>

Same listing as `apiList`, but each value carries the parent id. Use
when you need child → parent without fetching each item. See #310.

##### Parameters

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`Record`\<`string`, [`ListEntryWithParent`](../base/type-aliases/ListEntryWithParent.md)\<[`GanttCurriculum`](../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculum.md)\>\>\>

#### curriculum.apiSetAllocatedTime

> `readonly` **apiSetAllocatedTime**: (`itemId`, `containerId`, `allocatedTime`, `options?`) => `Promise`\<`void`\>

##### Parameters

###### itemId

`string`

###### containerId

`string`

###### allocatedTime

`number`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`void`\>

#### curriculum.apiUnlink

> `readonly` **apiUnlink**: (`itemId`, `oldParentId`, `options?`) => `Promise`\<`void`\>

##### Parameters

###### itemId

`string`

###### oldParentId

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`void`\>

#### curriculum.apiUpdate

> `readonly` **apiUpdate**: (`updates`, `options?`) => `Promise`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../base/type-aliases/BaseDocument.md)\>

##### Parameters

###### updates

`Partial`\<[`GanttCurriculum`](../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculum.md)\> & `object`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../base/type-aliases/BaseDocument.md)\>

### cut

> `readonly` **cut**: `object` = `curriculumCutApi`

#### cut.cut

> `readonly` **cut**: (`curriculumId`, `options`) => `Promise`\<[`ApiCurriculumCutResponse`](../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutResponse.md)\> = `cutCurriculumToSchedule`

POST /api/gantt/curriculums/[id]/cut — materialize a published, linked
curriculum into schedule events. Resolves to the cut summary, or throws a
[CurriculumCutError](../../../api-shared/types/gantt/cut/classes/CurriculumCutError.md) carrying the coded reason on a 4xx.

##### Parameters

###### curriculumId

`string`

###### options?

[`ApiCurriculumCutPayload`](../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPayload.md) = `{}`

##### Returns

`Promise`\<[`ApiCurriculumCutResponse`](../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutResponse.md)\>

#### cut.plan

> `readonly` **plan**: (`curriculumId`, `options`) => `Promise`\<[`ApiCurriculumCutPlanResponse`](../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPlanResponse.md)\> = `planCurriculumCut`

POST /api/gantt/curriculums/[id]/cut/plan — the "plan" half of the
plan-then-confirm flow. Runs the full cut pipeline without writing and
returns what it would do plus the open decisions the dialog must ask about.

##### Parameters

###### curriculumId

`string`

###### options?

[`ApiCurriculumCutPayload`](../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPayload.md) = `{}`

##### Returns

`Promise`\<[`ApiCurriculumCutPlanResponse`](../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPlanResponse.md)\>

#### cut.preview

> `readonly` **preview**: (`curriculumId`) => `Promise`\<[`ApiCurriculumCutPreviewResponse`](../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPreviewResponse.md)\> = `previewCurriculumCut`

GET /api/gantt/curriculums/[id]/cut/preview — dry-run of the cut planner:
dated, timed occurrences (or the planner's validation errors), no writes.

##### Parameters

###### curriculumId

`string`

##### Returns

`Promise`\<[`ApiCurriculumCutPreviewResponse`](../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPreviewResponse.md)\>

#### cut.pullBack

> `readonly` **pullBack**: (`curriculumId`) => `Promise`\<[`ApiCurriculumPullBackResponse`](../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumPullBackResponse.md)\> = `pullBackCurriculumSchedule`

DELETE /api/gantt/curriculums/[id]/cut — soft-delete every schedule event a
previous cut generated. Throws a [CurriculumPullBackError](../../../api-shared/types/gantt/cut/classes/CurriculumPullBackError.md) carrying the
coded reason on a 4xx.

##### Parameters

###### curriculumId

`string`

##### Returns

`Promise`\<[`ApiCurriculumPullBackResponse`](../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumPullBackResponse.md)\>

#### cut.reload

> `readonly` **reload**: (`curriculumId`, `options`) => `Promise`\<[`ApiCurriculumReloadResponse`](../../../api-shared/types/gantt/reload/type-aliases/ApiCurriculumReloadResponse.md)\> = `reloadCurriculumSchedule`

PATCH /api/gantt/curriculums/[id]/cut — reload an already-cut schedule from
the current gantt. With `dryRun` the server only computes the diff.

##### Parameters

###### curriculumId

`string`

Curriculum to reload from.

###### options?

[`ApiCurriculumReloadPayload`](../../../api-shared/types/gantt/reload/type-aliases/ApiCurriculumReloadPayload.md) = `{}`

##### Returns

`Promise`\<[`ApiCurriculumReloadResponse`](../../../api-shared/types/gantt/reload/type-aliases/ApiCurriculumReloadResponse.md)\>

#### cut.status

> `readonly` **status**: (`curriculumId`) => `Promise`\<[`ApiCurriculumCutStatus`](../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutStatus.md)\> = `getCurriculumCutStatus`

GET /api/gantt/curriculums/[id]/cut — whether the curriculum currently holds
live cut events, used to toggle between the "cut" and "pull back" actions.

##### Parameters

###### curriculumId

`string`

##### Returns

`Promise`\<[`ApiCurriculumCutStatus`](../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutStatus.md)\>

### day

> `readonly` **day**: [`BasicGantApi`](../base/type-aliases/BasicGantApi.md)\<[`GanttDay`](../../../api-shared/types/gantt/models/day/type-aliases/GanttDay.md), [`CreateGanttDayPayload`](../../../api-shared/types/gantt/create-payloads/type-aliases/CreateGanttDayPayload.md)\> = `dayApi`

### event

> `readonly` **event**: `object` = `moduleEventApi`

#### event.apiCreate

> `readonly` **apiCreate**: (`payload`, `options?`) => `Promise`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../base/type-aliases/BaseDocument.md)\>

##### Parameters

###### payload

[`CreateGanttEventPayload`](../../../api-shared/types/gantt/create-payloads/type-aliases/CreateGanttEventPayload.md)

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../base/type-aliases/BaseDocument.md)\>

#### event.apiDelete

> `readonly` **apiDelete**: (`id`, `options?`) => `Promise`\<`void`\>

##### Parameters

###### id

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`void`\>

#### event.apiDuplicate

> **apiDuplicate**: (`eventId`, `moduleId`) => `Promise`\<[`ModuleEventDocument`](../module-event/type-aliases/ModuleEventDocument.md)\>

##### Parameters

###### eventId

`string`

###### moduleId

`string`

##### Returns

`Promise`\<[`ModuleEventDocument`](../module-event/type-aliases/ModuleEventDocument.md)\>

#### event.apiGet

> `readonly` **apiGet**: (`id`, `options?`) => `Promise`\<[`ApiModuleEvent`](../../../api-shared/types/gantt/api-layer/type-aliases/ApiModuleEvent.md)\>

##### Parameters

###### id

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<[`ApiModuleEvent`](../../../api-shared/types/gantt/api-layer/type-aliases/ApiModuleEvent.md)\>

#### event.apiGetAllocatedTime

> `readonly` **apiGetAllocatedTime**: (`itemId`, `containerId`, `options?`) => `Promise`\<`number`\>

##### Parameters

###### itemId

`string`

###### containerId

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`number`\>

#### event.apiGetMany

> `readonly` **apiGetMany**: (`ids`, `options?`) => `Promise`\<`Record`\<`string`, `object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../base/type-aliases/BaseDocument.md)\>\>

##### Parameters

###### ids

`string`[]

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`Record`\<`string`, `object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../base/type-aliases/BaseDocument.md)\>\>

#### event.apiLink

> `readonly` **apiLink**: (`itemId`, `newParentId`, `options?`) => `Promise`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../base/type-aliases/BaseDocument.md)\>

##### Parameters

###### itemId

`string`

###### newParentId

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../base/type-aliases/BaseDocument.md)\>

#### event.apiList

> `readonly` **apiList**: (`options?`) => `Promise`\<`Record`\<`string`, `string`\>\>

##### Parameters

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`Record`\<`string`, `string`\>\>

#### event.apiListWithParents

> `readonly` **apiListWithParents**: (`options?`) => `Promise`\<`Record`\<`string`, [`ListEntryWithParent`](../base/type-aliases/ListEntryWithParent.md)\<[`GanttEvent`](../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)\>\>\>

Same listing as `apiList`, but each value carries the parent id. Use
when you need child → parent without fetching each item. See #310.

##### Parameters

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`Record`\<`string`, [`ListEntryWithParent`](../base/type-aliases/ListEntryWithParent.md)\<[`GanttEvent`](../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)\>\>\>

#### event.apiSetAllocatedTime

> `readonly` **apiSetAllocatedTime**: (`itemId`, `containerId`, `allocatedTime`, `options?`) => `Promise`\<`void`\>

##### Parameters

###### itemId

`string`

###### containerId

`string`

###### allocatedTime

`number`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`void`\>

#### event.apiUnlink

> `readonly` **apiUnlink**: (`itemId`, `oldParentId`, `options?`) => `Promise`\<`void`\>

##### Parameters

###### itemId

`string`

###### oldParentId

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`void`\>

#### event.apiUpdate

> `readonly` **apiUpdate**: (`updates`, `options?`) => `Promise`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../base/type-aliases/BaseDocument.md)\>

##### Parameters

###### updates

`Partial`\<[`GanttEvent`](../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)\> & `object`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../base/type-aliases/BaseDocument.md)\>

### execution

> `readonly` **execution**: `object` = `curriculumExecutionApi`

#### execution.get

> `readonly` **get**: (`curriculumId`) => `Promise`\<[`ApiCurriculumExecutionResponse`](../../../api-shared/types/gantt/execution/type-aliases/ApiCurriculumExecutionResponse.md)\> = `fetchCurriculumExecution`

GET /api/gantt/curriculums/[id]/execution — תכנון מול ביצוע comparison for a
curriculum. Resolves to `{ events: {} }` when the curriculum has not been
cut into a schedule yet.

##### Parameters

###### curriculumId

`string`

##### Returns

`Promise`\<[`ApiCurriculumExecutionResponse`](../../../api-shared/types/gantt/execution/type-aliases/ApiCurriculumExecutionResponse.md)\>

### getShuffleUsages

> `readonly` **getShuffleUsages**: (`syllabusId`, `names`) => `Promise`\<[`ShuffleUsages`](../../../api-shared/types/gantt/shuffles/type-aliases/ShuffleUsages.md)\> = `apiGetShuffleUsages`

Modules and events currently tagged with any of `names`.

#### Parameters

##### syllabusId

`string`

##### names

`string`[]

#### Returns

`Promise`\<[`ShuffleUsages`](../../../api-shared/types/gantt/shuffles/type-aliases/ShuffleUsages.md)\>

### mappings

> `readonly` **mappings**: `object` = `curriculumModuleDayMappingApi`

#### mappings.apiCreate

> `readonly` **apiCreate**: (`curriculumId`, `payload`, `options?`) => `Promise`\<[`GanttCurriculumEventDayMapping`](../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\> = `apiCreateModuleDayMapping`

POST: Creates a new module-to-day mapping.

##### Parameters

###### curriculumId

`string`

###### payload

[`CreateGanttCurriculumEventDayMapping`](../../../api-shared/types/gantt/create-payloads/type-aliases/CreateGanttCurriculumEventDayMapping.md)

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<[`GanttCurriculumEventDayMapping`](../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

#### mappings.apiDelete

> `readonly` **apiDelete**: (`curriculumId`, `moduleId`, `eventId`, `dayId`, `options?`) => `Promise`\<`void`\> = `apiDeleteModuleDayMapping`

DELETE: Removes a module-to-day mapping.

##### Parameters

###### curriculumId

`string`

###### moduleId

`string`

###### eventId

`string` \| `null`

###### dayId

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<`void`\>

#### mappings.apiGet

> `readonly` **apiGet**: (`curriculumId`, `dayId?`, `options?`) => `Promise`\<[`GanttCurriculumEventDayMapping`](../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)[]\> = `apiGetModuleDayMapping`

GET: Retrieves all module mappings for a curriculum.

##### Parameters

###### curriculumId

`string`

###### dayId?

`string` \| `string`[]

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<[`GanttCurriculumEventDayMapping`](../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)[]\>

#### mappings.apiUpdate

> `readonly` **apiUpdate**: (`curriculumId`, `moduleId`, `eventId`, `oldMapping`, `newValues`, `options?`) => `Promise`\<[`GanttCurriculumEventDayMapping`](../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\> = `apiUpdateModuleDayMapping`

PATCH: Updates an existing mapping or reorders it.

##### Parameters

###### curriculumId

`string`

###### moduleId

`string`

###### eventId

`string` \| `null`

###### oldMapping

###### dayId

`string`

###### newValues

###### dayId?

`string`

###### sortOrder?

`number`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<[`GanttCurriculumEventDayMapping`](../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

### module

> `readonly` **module**: [`BasicGantApi`](../base/type-aliases/BasicGantApi.md)\<[`GanttModule`](../../../api-shared/types/gantt/models/module/type-aliases/GanttModule.md), [`CreateGanttModulePayload`](../../../api-shared/types/gantt/create-payloads/type-aliases/CreateGanttModulePayload.md)\> = `moduleApi`

### recurrenceExceptions

> `readonly` **recurrenceExceptions**: `object` = `recurrenceExceptionApi`

#### recurrenceExceptions.apiDeleteOccurrence

> **apiDeleteOccurrence**: (`eventId`, `payload`, `options?`) => `Promise`\<[`GanttEventRecurrenceException`](../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md)\>

POST: Deletes a single recurring occurrence (excepts that day only).

##### Parameters

###### eventId

`string`

###### payload

###### curriculumId

`string`

###### dayId

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<[`GanttEventRecurrenceException`](../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md)\>

#### recurrenceExceptions.apiGet

> `readonly` **apiGet**: (`curriculumId`, `options?`) => `Promise`\<[`GanttEventRecurrenceException`](../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md)[]\> = `apiGetRecurrenceExceptions`

GET: Retrieves every recurrence exception for a curriculum.

##### Parameters

###### curriculumId

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<[`GanttEventRecurrenceException`](../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md)[]\>

#### recurrenceExceptions.apiMaterializeOccurrence

> **apiMaterializeOccurrence**: (`eventId`, `payload`, `options?`) => `Promise`\<\{ `event`: `object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & `object`; `mapping`: \{ `dayId`: `string`; `eventId`: `string`; `moduleId`: `string`; \}; \}\>

POST: Materializes a recurring occurrence into its own standalone event.

##### Parameters

###### eventId

`string`

###### payload

###### curriculumId

`string`

###### dayId

`string`

###### moduleId

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<\{ `event`: `object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & `object`; `mapping`: \{ `dayId`: `string`; `eventId`: `string`; `moduleId`: `string`; \}; \}\>

#### recurrenceExceptions.apiRestoreOccurrence

> **apiRestoreOccurrence**: (`eventId`, `payload`, `options?`) => `Promise`\<\{ `curriculumId`: `string`; `dayId`: `string`; `eventId`: `string`; \}\>

DELETE: Restores a previously skipped occurrence (#469).

##### Parameters

###### eventId

`string`

###### payload

###### curriculumId

`string`

###### dayId

`string`

###### options?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

##### Returns

`Promise`\<\{ `curriculumId`: `string`; `dayId`: `string`; `eventId`: `string`; \}\>

### reorderEvents

> `readonly` **reorderEvents**: (`moduleId`, `eventIds`) => `Promise`\<`void`\> = `apiReorderEvents`

#### Parameters

##### moduleId

`string`

##### eventIds

`string`[]

#### Returns

`Promise`\<`void`\>

### reorderModules

> `readonly` **reorderModules**: (`syllabusId`, `moduleIds`) => `Promise`\<`void`\> = `apiReorderModules`

#### Parameters

##### syllabusId

`string`

##### moduleIds

`string`[]

#### Returns

`Promise`\<`void`\>

### syllabus

> `readonly` **syllabus**: [`BasicGantApi`](../base/type-aliases/BasicGantApi.md)\<[`GanttSyllabus`](../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md), [`CreateGanttSyllabusPayload`](../../../api-shared/types/gantt/create-payloads/type-aliases/CreateGanttSyllabusPayload.md)\> = `syllabusApi`

### week

> `readonly` **week**: [`BasicGantApi`](../base/type-aliases/BasicGantApi.md)\<[`GanttWeek`](../../../api-shared/types/gantt/models/week/type-aliases/GanttWeek.md), [`CreateGanttWeekPayload`](../../../api-shared/types/gantt/create-payloads/type-aliases/CreateGanttWeekPayload.md)\> = `weekApi`
