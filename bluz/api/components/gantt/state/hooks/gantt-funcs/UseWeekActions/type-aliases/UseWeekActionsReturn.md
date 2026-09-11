[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/state/hooks/gantt-funcs/UseWeekActions](../index.md) / UseWeekActionsReturn

# Type Alias: UseWeekActionsReturn

> **UseWeekActionsReturn** = `object`

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/UseWeekActions.tsx:25](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/hooks/gantt-funcs/UseWeekActions.tsx#L25)

## Properties

### createDay

> **createDay**: (`payload`) => `Promise`\<[`GanttDay`](../../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDay.md)\>

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/UseWeekActions.tsx:35](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/hooks/gantt-funcs/UseWeekActions.tsx#L35)

#### Parameters

##### payload

[`CreateGanttDayPayload`](../../../../../../../api-shared/types/gantt/create-payloads/type-aliases/CreateGanttDayPayload.md)

#### Returns

`Promise`\<[`GanttDay`](../../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDay.md)\>

***

### createWeek

> **createWeek**: (`payload`) => `Promise`\<[`GanttWeek`](../../../../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeek.md)\>

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/UseWeekActions.tsx:26](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/hooks/gantt-funcs/UseWeekActions.tsx#L26)

#### Parameters

##### payload

[`CreateGanttWeekPayload`](../../../../../../../api-shared/types/gantt/create-payloads/type-aliases/CreateGanttWeekPayload.md)

#### Returns

`Promise`\<[`GanttWeek`](../../../../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeek.md)\>

***

### deleteDay

> **deleteDay**: (`dayId`) => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/UseWeekActions.tsx:40](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/hooks/gantt-funcs/UseWeekActions.tsx#L40)

#### Parameters

##### dayId

[`GanttDayId`](../../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)

#### Returns

`Promise`\<`void`\>

***

### deleteWeek

> **deleteWeek**: (`weekId`, `curriculumId`) => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/UseWeekActions.tsx:31](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/hooks/gantt-funcs/UseWeekActions.tsx#L31)

#### Parameters

##### weekId

[`GanttWeekId`](../../../../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeekId.md)

##### curriculumId

[`GanttCurriculumId`](../../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md)

#### Returns

`Promise`\<`void`\>

***

### updateDay

> **updateDay**: (`dayId`, `updates`) => `Promise`\<[`GanttDay`](../../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDay.md)\>

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/UseWeekActions.tsx:36](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/hooks/gantt-funcs/UseWeekActions.tsx#L36)

#### Parameters

##### dayId

[`GanttDayId`](../../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)

##### updates

`Partial`\<[`GanttDay`](../../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDay.md)\>

#### Returns

`Promise`\<[`GanttDay`](../../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDay.md)\>

***

### updateWeek

> **updateWeek**: (`weekId`, `updates`) => `Promise`\<[`GanttWeek`](../../../../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeek.md)\>

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/UseWeekActions.tsx:27](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/hooks/gantt-funcs/UseWeekActions.tsx#L27)

#### Parameters

##### weekId

[`GanttWeekId`](../../../../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeekId.md)

##### updates

`Partial`\<\{ `comment?`: `string`; `weekendDuty?`: `boolean`; \}\>

#### Returns

`Promise`\<[`GanttWeek`](../../../../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeek.md)\>
