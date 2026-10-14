[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/constraint](../index.md) / getConstraintsByEvent

# Function: getConstraintsByEvent()

> **getConstraintsByEvent**(`constraints`, `eventIdsByModule`): `Record`\<`string`, [`GanttConstraint`](../type-aliases/GanttConstraint.md)[]\>

Defined in: [ui/src/api-shared/types/gantt/models/constraint.ts:119](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/models/constraint.ts#L119)

Every constraint that binds each event: its own plus those of every module
containing it. Events don't carry their constraints in the curriculum
payload, and a module's day constraint applies to all its events, so
recurrence echoing must resolve them here rather than read `event.constraints`.

## Parameters

### constraints

`Iterable`\<[`GanttConstraint`](../type-aliases/GanttConstraint.md) \| `undefined`\>

### eventIdsByModule

`Record`\<`string`, `ReadonlyArray`\<`string`\> \| `undefined`\>

## Returns

`Record`\<`string`, [`GanttConstraint`](../type-aliases/GanttConstraint.md)[]\>
