[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types](../index.md) / GanttContextType

# Type Alias: GanttContextType

> **GanttContextType** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:15](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L15)

## Properties

### allLinearDays

> **allLinearDays**: `string`[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:24](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L24)

Every day of the timeline, even while a week is zoomed.

***

### curriculumMappings

> **curriculumMappings**: `Record`\<`string`, [`GanttCurriculumEventDayMapping`](../../../../../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:38](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L38)

***

### dateOfDayId

> **dateOfDayId**: (`dayId`) => `string` \| `undefined`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:35](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L35)

Calendar date of a timeline day as "YYYY-MM-DD", or undefined when the
curriculum has no start date. Drives the recurrence window (#468).

#### Parameters

##### dayId

`string`

#### Returns

`string` \| `undefined`

***

### dayCellWidth

> **dayCellWidth**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:49](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L49)

Pixel width of a single day/week column. Widens when a week is zoomed (#90).

***

### dayIndexMap

> **dayIndexMap**: `Map`\<`string`, `number`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:28](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L28)

O(1) lookup of a dayId's position within linearDays (#159).

***

### eventMappings

> **eventMappings**: `Record`\<`string`, `string`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:36](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L36)

***

### eventSpans

> **eventSpans**: `Record`\<`string`, [`EventDaySpan`](../../../../../gantt-time-utils/type-aliases/EventDaySpan.md)\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:40](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L40)

Days each mapped event occupies once multi-day spillover is applied (#105).

***

### getDropWarning

> **getDropWarning**: (`payload`, `target`) => `null` \| `string`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:98](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L98)

While dragging: why dropping the dragged item (dnd `active.data`) on a
cell (its droppable data) would be a problem, or null (#811).

#### Parameters

##### payload

`Record`\<`string`, `unknown`\> \| `undefined`

##### target

`Record`\<`string`, `unknown`\> \| `undefined`

#### Returns

`null` \| `string`

***

### ignoreBreaks

> **ignoreBreaks**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:26](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L26)

Page toggle: leave break events (meals…) out of every time total.

***

### isEventVisible

> **isEventVisible**: (`eventId`) => `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:73](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L73)

#### Parameters

##### eventId

`string`

#### Returns

`boolean`

***

### isModuleExpanded

> **isModuleExpanded**: (`moduleId`) => `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:64](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L64)

Per-module expand/collapse state, lifted so a chip can reveal an event row.

#### Parameters

##### moduleId

`string`

#### Returns

`boolean`

***

### isModuleVisible

> **isModuleVisible**: (`moduleId`) => `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:72](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L72)

#### Parameters

##### moduleId

`string`

#### Returns

`boolean`

***

### isSyllabusExpanded

> **isSyllabusExpanded**: (`syllabusId`) => `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:61](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L61)

Per-syllabus expand/collapse state, lifted so all rows can be toggled at once (#91).

#### Parameters

##### syllabusId

`string`

#### Returns

`boolean`

***

### isSyllabusVisible

> **isSyllabusVisible**: (`syllabusId`) => `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:71](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L71)

First-column search predicates: whether a row survives the active filter (#323).

#### Parameters

##### syllabusId

`string`

#### Returns

`boolean`

***

### linearDays

> **linearDays**: `string`[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:22](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L22)

***

### moduleMappings

> **moduleMappings**: `Record`\<`string`, `string`[]\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:37](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L37)

***

### onMapEvent

> **onMapEvent**: (`moduleId`, `eventId`, `dayId`) => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:76](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L76)

#### Parameters

##### moduleId

`string`

##### eventId

`string`

##### dayId

`string`

#### Returns

`Promise`\<`void`\>

***

### onMapModule

> **onMapModule**: (`moduleId`, `dayId`) => `Promise`\<(`null` \| `string`)[]\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:75](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L75)

Resolves to the event ids it mapped (null for a module-level mapping).

#### Parameters

##### moduleId

`string`

##### dayId

`string`

#### Returns

`Promise`\<(`null` \| `string`)[]\>

***

### onMoveEvent

> **onMoveEvent**: (`moduleId`, `eventId`, `sourceDayId`, `targetDayId`) => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:81](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L81)

#### Parameters

##### moduleId

`string`

##### eventId

`string`

##### sourceDayId

`string`

##### targetDayId

`string`

#### Returns

`Promise`\<`void`\>

***

### onMoveModule

> **onMoveModule**: (`moduleId`, `sourceDayId`, `targetDayId`) => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:87](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L87)

#### Parameters

##### moduleId

`string`

##### sourceDayId

`string`

##### targetDayId

`string`

#### Returns

`Promise`\<`void`\>

***

### onShiftModule

> **onShiftModule**: (`moduleId`, `deltaDays`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:93](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L93)

Resolves false when nothing moved (the shift would leave the timeline).

#### Parameters

##### moduleId

`string`

##### deltaDays

`number`

#### Returns

`Promise`\<`boolean`\>

***

### relativeDaySizing

> **relativeDaySizing**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:19](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L19)

Weekly view only: size/position blocks by the day they occupy instead of filling the whole cell.

***

### scheduledMinutesByDay

> **scheduledMinutesByDay**: `Record`\<`string`, `number`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:42](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L42)

Per-day scheduled minutes with spillover subtracted/added per day (#105).

***

### searchActive

> **searchActive**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:69](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L69)

True while the first-column search filter is narrowing the row tree (#323).

***

### setAllRows

> **setAllRows**: (`open`, `syllabusKeys`, `moduleKeys`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:67](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L67)

Opens or closes every row: syllabus/shuffle keys first, module keys second.

#### Parameters

##### open

`boolean`

##### syllabusKeys

`string`[]

##### moduleKeys

`string`[]

#### Returns

`void`

***

### setWeeklyView

> **setWeeklyView**: (`weeklyView`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:17](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L17)

#### Parameters

##### weeklyView

`boolean`

#### Returns

`void`

***

### setZoomedWeekId

> **setZoomedWeekId**: (`weekId`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:54](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L54)

#### Parameters

##### weekId

`null` \| `string`

#### Returns

`void`

***

### singleWeekDayZoom

> **singleWeekDayZoom**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:53](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L53)

True when a single week is zoomed in day view: header shows allocated/available time and blocks are sized by their required time.

***

### startDate

> **startDate**: `null` \| `string`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:20](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L20)

***

### studentLoadByDay

> **studentLoadByDay**: `Record`\<`string`, [`DayStudentLoad`](../../../../../student-load/type-aliases/DayStudentLoad.md)\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:44](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L44)

Per-day scheduled time per student path, with alignment issues.

***

### studentPaths

> **studentPaths**: [`StudentPath`](../../../../../student-load/type-aliases/StudentPath.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:46](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L46)

The student paths `studentLoadByDay` is broken down by.

***

### timelineWeeks

> **timelineWeeks**: [`GanttWeek`](../../../../../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeek.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:21](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L21)

***

### toggleModule

> **toggleModule**: (`moduleId`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:65](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L65)

#### Parameters

##### moduleId

`string`

#### Returns

`void`

***

### toggleSyllabus

> **toggleSyllabus**: (`syllabusId`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:62](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L62)

#### Parameters

##### syllabusId

`string`

#### Returns

`void`

***

### violations

> **violations**: `Record`\<`string`, `string`[]\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:47](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L47)

***

### weekIndexByDayId

> **weekIndexByDayId**: `Map`\<`string`, `number`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:30](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L30)

O(1) lookup of a dayId's owning week index within timelineWeeks (#159).

***

### weekIndexOffset

> **weekIndexOffset**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:59](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L59)

Absolute index of the first visible week within the full timeline. Non-zero
only while zoomed, so date labels stay correct when the grid is filtered (#90).

***

### weeklyView

> **weeklyView**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:16](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L16)

***

### zoomedWeekId

> **zoomedWeekId**: `null` \| `string`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:51](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L51)

Id of the week currently zoomed to full width, or null (days view only, #90).
