[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/shuffle-alignment](../index.md) / validateShuffleAlignment

# Function: validateShuffleAlignment()

> **validateShuffleAlignment**(`source`, `controller`): `Promise`\<[`AlignmentViolation`](../../../api-shared/shuffle-alignment/type-aliases/AlignmentViolation.md)[]\>

Defined in: [ui/src/api-server/shuffle-alignment.ts:23](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/shuffle-alignment.ts#L23)

Runs the shared R-50/R-51 check (#1000) over the live calendar in a range,
a saved draft, or events sent inline (an unsaved draft). Course and subject
names only label the result, so a Hive outage degrades to subject ids.
The schedule validator (`schedule-validation.ts`) runs the same check as
two of its rules; this keeps the original route and the CLI working.

## Parameters

### source

[`ScheduleSource`](../../schedule-validation/type-aliases/ScheduleSource.md)

### controller

[`DatabaseController`](../../mongo-db-controller/classes/DatabaseController.md)

## Returns

`Promise`\<[`AlignmentViolation`](../../../api-shared/shuffle-alignment/type-aliases/AlignmentViolation.md)[]\>
