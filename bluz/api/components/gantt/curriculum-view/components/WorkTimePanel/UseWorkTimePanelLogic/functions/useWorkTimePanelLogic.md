[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/components/WorkTimePanel/UseWorkTimePanelLogic](../index.md) / useWorkTimePanelLogic

# Function: useWorkTimePanelLogic()

> **useWorkTimePanelLogic**(`curriculumId`, `curriculumWeekIds`, `localWeekIds`, `setLocalWeekIds`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/UseWorkTimePanelLogic.ts:14](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/UseWorkTimePanelLogic.ts#L14)

## Parameters

### curriculumId

`string` \| `null`

### curriculumWeekIds

`string`[]

### localWeekIds

`string`[]

### setLocalWeekIds

`Dispatch`\<`SetStateAction`\<`string`[]\>\>

## Returns

`object`

### buildDefaultWeekDays

> **buildDefaultWeekDays**: () => `Partial`\<[`GanttDay`](../../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDay.md)\>[]

#### Returns

`Partial`\<[`GanttDay`](../../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDay.md)\>[]

### onHoursKeyDown

> **onHoursKeyDown**: (`event`) => `void`

#### Parameters

##### event

`KeyboardEvent`\<`HTMLInputElement`\>

#### Returns

`void`

### onWeekCommentKeyDown

> **onWeekCommentKeyDown**: (`event`) => `void`

#### Parameters

##### event

`KeyboardEvent`\<`HTMLInputElement`\>

#### Returns

`void`

### persistWeeks

> **persistWeeks**: (`updatedWeekIds`) => `Promise`\<`void`\>

#### Parameters

##### updatedWeekIds

`string`[]

#### Returns

`Promise`\<`void`\>

### pickNextDay

> **pickNextDay**: (`dayNameSet`) => [`GanttDayIndex`](../../../../../../../api-shared/types/gantt/models/day/enumerations/GanttDayIndex.md) \| `null`

#### Parameters

##### dayNameSet

`Set`\<[`GanttDayIndex`](../../../../../../../api-shared/types/gantt/models/day/enumerations/GanttDayIndex.md)\>

#### Returns

[`GanttDayIndex`](../../../../../../../api-shared/types/gantt/models/day/enumerations/GanttDayIndex.md) \| `null`

### saveDayComment

> **saveDayComment**: () => `Promise`\<`void`\>

#### Returns

`Promise`\<`void`\>

### saveDayHours

> **saveDayHours**: () => `Promise`\<`void`\>

#### Returns

`Promise`\<`void`\>

### saveWeekComment

> **saveWeekComment**: () => `Promise`\<`void`\>

#### Returns

`Promise`\<`void`\>

### updateWeeksLocally

> **updateWeeksLocally**: (`updater`) => `void`

#### Parameters

##### updater

(`weekIds`) => `string`[]

#### Returns

`void`
