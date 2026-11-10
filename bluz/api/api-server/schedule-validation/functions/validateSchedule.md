[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/schedule-validation](../index.md) / validateSchedule

# Function: validateSchedule()

> **validateSchedule**(`source`, `controller`): `Promise`\<[`RuleViolation`](../../../api-shared/schedule-validation/types/type-aliases/RuleViolation.md)[]\>

Defined in: [ui/src/api-server/schedule-validation.ts:199](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/schedule-validation.ts#L199)

Every rule, in order — for callers that want the whole report at once (the CLI).

## Parameters

### source

[`ScheduleSource`](../type-aliases/ScheduleSource.md)

### controller

[`DatabaseController`](../../mongo-db-controller/classes/DatabaseController.md)

## Returns

`Promise`\<[`RuleViolation`](../../../api-shared/schedule-validation/types/type-aliases/RuleViolation.md)[]\>
