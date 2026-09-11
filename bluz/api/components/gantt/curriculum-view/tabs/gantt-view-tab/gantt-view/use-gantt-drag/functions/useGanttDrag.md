[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-drag](../index.md) / useGanttDrag

# Function: useGanttDrag()

> **useGanttDrag**(`__namedParameters`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-drag.ts:24](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-drag.ts#L24)

## Parameters

### \_\_namedParameters

`UseGanttDragArgs`

## Returns

`object`

### handleDragEnd

> **handleDragEnd**: (`event`) => `Promise`\<`void`\>

#### Parameters

##### event

`DragEndEvent`

#### Returns

`Promise`\<`void`\>

### handleMapEvent

> **handleMapEvent**: (`moduleId`, `eventId`, `dayId`) => `Promise`\<`void`\>

#### Parameters

##### moduleId

`string`

##### eventId

`string`

##### dayId

`string`

#### Returns

`Promise`\<`void`\>

### handleMapModule

> **handleMapModule**: (`moduleId`, `dayId`) => `Promise`\<`void`\>

#### Parameters

##### moduleId

`string`

##### dayId

`string`

#### Returns

`Promise`\<`void`\>

### handleMoveEvent

> **handleMoveEvent**: (`moduleId`, `eventId`, `sourceDayId`, `targetDayId`) => `Promise`\<`void`\>

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

### handleMoveModule

> **handleMoveModule**: (`moduleId`, `sourceDayId`, `targetDayId`) => `Promise`\<`void`\>

#### Parameters

##### moduleId

`string`

##### sourceDayId

`string`

##### targetDayId

`string`

#### Returns

`Promise`\<`void`\>

### handleShiftModule

> **handleShiftModule**: (`moduleId`, `deltaDays`) => `Promise`\<`void`\>

#### Parameters

##### moduleId

`string`

##### deltaDays

`number`

#### Returns

`Promise`\<`void`\>
