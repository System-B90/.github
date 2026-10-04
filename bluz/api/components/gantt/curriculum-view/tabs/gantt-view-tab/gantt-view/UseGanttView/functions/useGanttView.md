[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/UseGanttView](../index.md) / useGanttView

# Function: useGanttView()

> **useGanttView**(`curriculumId`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/UseGanttView.ts:37](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/UseGanttView.ts#L37)

## Parameters

### curriculumId

`string`

## Returns

`object`

### activeLinks

> **activeLinks**: [`ConstraintLink`](../../types/type-aliases/ConstraintLink.md)[]

### allCollapsed

> **allCollapsed**: `boolean`

### collapseAllSyllabuses

> **collapseAllSyllabuses**: () => `void`

#### Returns

`void`

### containerRef

> **containerRef**: `RefObject`\<`HTMLDivElement` \| `null`\>

### contextValue

> **contextValue**: `object`

#### contextValue.allLinearDays

> **allLinearDays**: `string`[]

#### contextValue.curriculumMappings

> **curriculumMappings**: `Record`\<`string`, [`GanttCurriculumEventDayMapping`](../../../../../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

#### contextValue.dateOfDayId

> **dateOfDayId**: (`dayId`) => `string` \| `undefined`

##### Parameters

###### dayId

`string`

##### Returns

`string` \| `undefined`

#### contextValue.dayCellWidth

> **dayCellWidth**: `number`

#### contextValue.dayIndexMap

> **dayIndexMap**: `Map`\<`string`, `number`\>

#### contextValue.eventMappings

> **eventMappings**: `object`

##### Index Signature

\[`key`: `string`\]: `string`

#### contextValue.eventSpans

> **eventSpans**: `Record`\<`string`, [`EventDaySpan`](../../../../../gantt-time-utils/type-aliases/EventDaySpan.md)\>

#### contextValue.getDropWarning

> **getDropWarning**: (`payload`, `target`) => `string` \| `null`

##### Parameters

###### payload

`Record`\<`string`, `unknown`\> \| `undefined`

###### target

`Record`\<`string`, `unknown`\> \| `undefined`

##### Returns

`string` \| `null`

#### contextValue.ignoreBreaks

> **ignoreBreaks**: `boolean`

#### contextValue.isEventVisible

> **isEventVisible**: (`eventId`) => `boolean`

##### Parameters

###### eventId

`string`

##### Returns

`boolean`

#### contextValue.isModuleExpanded

> **isModuleExpanded**: (`moduleId`) => `boolean`

##### Parameters

###### moduleId

`string`

##### Returns

`boolean`

#### contextValue.isModuleVisible

> **isModuleVisible**: (`moduleId`) => `boolean`

##### Parameters

###### moduleId

`string`

##### Returns

`boolean`

#### contextValue.isSyllabusExpanded

> **isSyllabusExpanded**: (`syllabusId`) => `boolean`

##### Parameters

###### syllabusId

`string`

##### Returns

`boolean`

#### contextValue.isSyllabusVisible

> **isSyllabusVisible**: (`syllabusId`) => `boolean`

##### Parameters

###### syllabusId

`string`

##### Returns

`boolean`

#### contextValue.linearDays

> **linearDays**: `string`[]

#### contextValue.moduleMappings

> **moduleMappings**: `Record`\<`string`, `string`[]\>

#### contextValue.onMapEvent

> **onMapEvent**: (`moduleId`, `eventId`, `dayId`) => `Promise`\<`void`\> = `handleMapEvent`

##### Parameters

###### moduleId

`string`

###### eventId

`string`

###### dayId

`string`

##### Returns

`Promise`\<`void`\>

#### contextValue.onMapModule

> **onMapModule**: (`moduleId`, `dayId`) => `Promise`\<(`string` \| `null`)[]\> = `handleMapModule`

##### Parameters

###### moduleId

`string`

###### dayId

`string`

##### Returns

`Promise`\<(`string` \| `null`)[]\>

#### contextValue.onMoveEvent

> **onMoveEvent**: (`moduleId`, `eventId`, `sourceDayId`, `targetDayId`) => `Promise`\<`void`\> = `handleMoveEvent`

##### Parameters

###### moduleId

`string`

###### eventId

`string`

###### sourceDayId

`string`

###### targetDayId

`string`

##### Returns

`Promise`\<`void`\>

#### contextValue.onMoveModule

> **onMoveModule**: (`moduleId`, `sourceDayId`, `targetDayId`) => `Promise`\<`void`\> = `handleMoveModule`

##### Parameters

###### moduleId

`string`

###### sourceDayId

`string`

###### targetDayId

`string`

##### Returns

`Promise`\<`void`\>

#### contextValue.onShiftModule

> **onShiftModule**: (`moduleId`, `deltaDays`) => `Promise`\<`boolean`\> = `handleShiftModule`

##### Parameters

###### moduleId

`string`

###### deltaDays

`number`

##### Returns

`Promise`\<`boolean`\>

#### contextValue.relativeDaySizing

> **relativeDaySizing**: `boolean`

#### contextValue.scheduledMinutesByDay

> **scheduledMinutesByDay**: `Record`\<`string`, `number`\>

#### contextValue.searchActive

> **searchActive**: `boolean`

#### contextValue.setAllRows

> **setAllRows**: (`open`, `syllabusKeys`, `moduleKeys`) => `void`

##### Parameters

###### open

`boolean`

###### syllabusKeys

`string`[]

###### moduleKeys

`string`[]

##### Returns

`void`

#### contextValue.setWeeklyView

> **setWeeklyView**: (`next`) => `void`

##### Parameters

###### next

`boolean`

##### Returns

`void`

#### contextValue.setZoomedWeekId

> **setZoomedWeekId**: `Dispatch`\<`SetStateAction`\<`string` \| `null`\>\>

#### contextValue.singleWeekDayZoom

> **singleWeekDayZoom**: `boolean`

#### contextValue.startDate

> **startDate**: `string` \| `null`

#### contextValue.studentLoadByDay

> **studentLoadByDay**: `Record`\<`string`, [`DayStudentLoad`](../../../../../student-load/type-aliases/DayStudentLoad.md)\>

#### contextValue.studentPaths

> **studentPaths**: [`StudentPath`](../../../../../student-load/type-aliases/StudentPath.md)[]

#### contextValue.timelineWeeks

> **timelineWeeks**: [`GanttWeek`](../../../../../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeek.md)[]

#### contextValue.toggleModule

> **toggleModule**: (`moduleId`) => `void`

##### Parameters

###### moduleId

`string`

##### Returns

`void`

#### contextValue.toggleSyllabus

> **toggleSyllabus**: (`syllabusId`) => `void`

##### Parameters

###### syllabusId

`string`

##### Returns

`void`

#### contextValue.violations

> **violations**: `Record`\<`string`, `string`[]\>

#### contextValue.weekIndexByDayId

> **weekIndexByDayId**: `Map`\<`string`, `number`\>

#### contextValue.weekIndexOffset

> **weekIndexOffset**: `number`

#### contextValue.weeklyView

> **weeklyView**: `boolean`

#### contextValue.zoomedWeekId

> **zoomedWeekId**: `string` \| `null`

### curriculum

> **curriculum**: [`GanttCurriculumDocument`](../../../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md)

### dragLabels

> **dragLabels**: [`DragLabels`](../../drag-labels/type-aliases/DragLabels.md)

### expandAllSyllabuses

> **expandAllSyllabuses**: () => `void`

#### Returns

`void`

### handleDragEnd

> **handleDragEnd**: (`event`) => `Promise`\<`void`\>

#### Parameters

##### event

`DragEndEvent`

#### Returns

`Promise`\<`void`\>

### handleWeeklyViewChange

> **handleWeeklyViewChange**: (`checked`) => `void`

#### Parameters

##### checked

`boolean`

#### Returns

`void`

### ignoreBreaks

> **ignoreBreaks**: `boolean`

### relativeDaySizing

> **relativeDaySizing**: `boolean`

### revealItem

> **revealItem**: (`syllabusId`, `moduleId`, `eventId?`) => `void`

#### Parameters

##### syllabusId

`string`

##### moduleId

`string`

##### eventId?

`string`

#### Returns

`void`

### searchQuery

> **searchQuery**: `string`

### setIgnoreBreaks

> **setIgnoreBreaks**: (`next`) => `void`

#### Parameters

##### next

`boolean`

#### Returns

`void`

### setRelativeDaySizing

> **setRelativeDaySizing**: (`next`) => `void`

#### Parameters

##### next

`boolean`

#### Returns

`void`

### setSearchQuery

> **setSearchQuery**: `Dispatch`\<`SetStateAction`\<`string`\>\>

### setShowConstraints

> **setShowConstraints**: (`next`) => `void`

#### Parameters

##### next

`boolean`

#### Returns

`void`

### setShowUnallocated

> **setShowUnallocated**: (`next`) => `void`

#### Parameters

##### next

`boolean`

#### Returns

`void`

### setZoomedWeekId

> **setZoomedWeekId**: `Dispatch`\<`SetStateAction`\<`string` \| `null`\>\>

### showConstraints

> **showConstraints**: `boolean`

### showUnallocated

> **showUnallocated**: `boolean`

### unallocatedBySyllabus

> **unallocatedBySyllabus**: `object`[]

### unallocatedCount

> **unallocatedCount**: `number`

### weeklyView

> **weeklyView**: `boolean`

### zoomedWeekId

> **zoomedWeekId**: `string` \| `null`
