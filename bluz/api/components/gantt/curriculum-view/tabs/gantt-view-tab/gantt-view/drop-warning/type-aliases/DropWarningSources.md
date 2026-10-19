[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning](../index.md) / DropWarningSources

# Type Alias: DropWarningSources

> **DropWarningSources** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts:19](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts#L19)

## Properties

### alignment?

> `optional` **alignment?**: `Omit`\<[`AlignmentSources`](../../shuffle-alignment/type-aliases/AlignmentSources.md), `"eventMappings"`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts:29](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts#L29)

Shuffle names, module → syllabus and event details for the alignment check (#886).

***

### constraints

> **constraints**: `Readonly`\<`Record`\<`string`, [`GanttConstraint`](../../../../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md) \| `undefined`\>\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts:20](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts#L20)

***

### days

> **days**: `Readonly`\<`Record`\<`string`, \{ `dayIndex`: [`GanttDayIndex`](../../../../../../../../api-shared/types/gantt/models/day/enumerations/GanttDayIndex.md); \} \| `undefined`\>\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts:23](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts#L23)

***

### eventMappings

> **eventMappings**: `Record`\<`string`, `string`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts:24](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts#L24)

***

### events

> **events**: `Readonly`\<`Record`\<`string`, `Constrained`\>\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts:22](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts#L22)

***

### linearDays

> **linearDays**: `ReadonlyArray`\<`string`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts:25](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts#L25)

***

### modules

> **modules**: `Readonly`\<`Record`\<`string`, `Constrained` & `object` \| `undefined`\>\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts:21](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts#L21)

***

### planShift

> **planShift**: (`moduleId`, `deltaDays`) => `object`[] \| `null`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts:27](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drop-warning.ts#L27)

Null when the shift would push an event off the timeline.

#### Parameters

##### moduleId

`string`

##### deltaDays

`number`

#### Returns

`object`[] \| `null`
