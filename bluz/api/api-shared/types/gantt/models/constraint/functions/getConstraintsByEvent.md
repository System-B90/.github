[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/constraint](../index.md) / getConstraintsByEvent

# Function: getConstraintsByEvent()

> **getConstraintsByEvent**(`constraints`, `eventIdsByModule`): `Record`\<`string`, [`GanttConstraint`](../type-aliases/GanttConstraint.md)[]\>

Defined in: [ui/src/api-shared/types/gantt/models/constraint.ts:126](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/gantt/models/constraint.ts#L126)

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
