[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-zoom](../index.md) / useGanttZoom

# Function: useGanttZoom()

> **useGanttZoom**(`__namedParameters`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-zoom.ts:21](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-zoom.ts#L21)

## Parameters

### \_\_namedParameters

`UseGanttZoomArgs`

## Returns

### allLinearDays

> **allLinearDays**: `string`[]

### allTimelineWeeks

> **allTimelineWeeks**: [`GanttWeek`](../../../../../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeek.md)[]

### containerRef

> **containerRef**: `RefObject`\<`HTMLDivElement` \| `null`\>

### dayCellWidth

> **dayCellWidth**: `number`

### dayIndexMap

> **dayIndexMap**: `Map`\<`string`, `number`\>

### handleWeeklyViewChange

> **handleWeeklyViewChange**: (`checked`) => `void`

#### Parameters

##### checked

`boolean`

#### Returns

`void`

### linearDays

> **linearDays**: `string`[]

### setWeeklyView

> **setWeeklyView**: (`next`) => `void`

#### Parameters

##### next

`boolean`

#### Returns

`void`

### setZoomedWeekId

> **setZoomedWeekId**: `Dispatch`\<`SetStateAction`\<`string` \| `null`\>\>

### singleWeekDayZoom

> **singleWeekDayZoom**: `boolean`

### stepZoomedWeek

> **stepZoomedWeek**: (`delta`) => `void`

Move the zoomed week by `delta` weeks, clamped to the curriculum. In
day view without a zoomed week yet, the first step picks a week to zoom
(stepping forward starts at the first week, back at the last).

#### Parameters

##### delta

`number`

#### Returns

`void`

### timelineWeeks

> **timelineWeeks**: [`GanttWeek`](../../../../../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeek.md)[]

### weekIndexByDayId

> **weekIndexByDayId**: `Map`\<`string`, `number`\>

### weekIndexOffset

> **weekIndexOffset**: `number`

### weeklyView

> **weeklyView**: `boolean`

### zoomedWeekId

> **zoomedWeekId**: `string` \| `null`
