[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning](../index.md) / DropWarningSources

# Type Alias: DropWarningSources

> **DropWarningSources** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts:18](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts#L18)

## Properties

### constraints

> **constraints**: `Readonly`\<`Record`\<`string`, [`GanttConstraint`](../../../../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md) \| `undefined`\>\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts:19](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts#L19)

***

### days

> **days**: `Readonly`\<`Record`\<`string`, \{ `dayIndex`: [`GanttDayIndex`](../../../../../../../../api-shared/types/gantt/models/day/enumerations/GanttDayIndex.md); \} \| `undefined`\>\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts:22](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts#L22)

***

### eventMappings

> **eventMappings**: `Record`\<`string`, `string`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts:23](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts#L23)

***

### events

> **events**: `Readonly`\<`Record`\<`string`, `Constrained`\>\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts:21](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts#L21)

***

### linearDays

> **linearDays**: `ReadonlyArray`\<`string`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts:24](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts#L24)

***

### modules

> **modules**: `Readonly`\<`Record`\<`string`, `Constrained` & `object` \| `undefined`\>\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts:20](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts#L20)

***

### planShift

> **planShift**: (`moduleId`, `deltaDays`) => `object`[] \| `null`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts:26](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts#L26)

Null when the shift would push an event off the timeline.

#### Parameters

##### moduleId

`string`

##### deltaDays

`number`

#### Returns

`object`[] \| `null`
