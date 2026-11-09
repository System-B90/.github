[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-violations](../index.md) / useGanttViolations

# Function: useGanttViolations()

> **useGanttViolations**(`__namedParameters`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-violations.ts:41](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-violations.ts#L41)

## Parameters

### \_\_namedParameters

#### constraints

`Record`\<`string`, [`GanttConstraint`](../../../../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)\>

#### days

`Record`\<`string`, `object` & [`BaseGantItem`](../../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md) & `object`\>

#### eventMappings

`Record`\<`string`, `string`\>

#### events

`Record`\<`string`, [`GanttEvent`](../../../../../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)\>

#### linearDays

`string`[]

#### moduleMappings

`Record`\<`string`, `string`[]\>

#### modules

`Record`\<`string`, [`GanttModule`](../../../../../../../../api-shared/types/gantt/models/module/type-aliases/GanttModule.md)\>

## Returns

`object`

### activeLinks

> **activeLinks**: [`ConstraintLink`](../../types/type-aliases/ConstraintLink.md)[] = `links`

### violations

> **violations**: `Record`\<`string`, `string`[]\> = `v`
