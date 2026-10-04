[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-drag](../index.md) / useGanttDrag

# Function: useGanttDrag()

> **useGanttDrag**(`__namedParameters`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-drag.ts:40](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-drag.ts#L40)

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

> **handleMapModule**: (`moduleId`, `dayId`) => `Promise`\<(`string` \| `null`)[]\>

#### Parameters

##### moduleId

`string`

##### dayId

`string`

#### Returns

`Promise`\<(`string` \| `null`)[]\>

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

> **handleShiftModule**: (`moduleId`, `deltaDays`) => `Promise`\<`boolean`\>

#### Parameters

##### moduleId

`string`

##### deltaDays

`number`

#### Returns

`Promise`\<`boolean`\>

### planShift

> **planShift**: (`moduleId`, `deltaDays`) => [`MappingMove`](../../module-drag/type-aliases/MappingMove.md)[] \| `null`

#### Parameters

##### moduleId

`string`

##### deltaDays

`number`

#### Returns

[`MappingMove`](../../module-drag/type-aliases/MappingMove.md)[] \| `null`
