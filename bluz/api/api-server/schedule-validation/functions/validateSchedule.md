[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/schedule-validation](../index.md) / validateSchedule

# Function: validateSchedule()

> **validateSchedule**(`source`, `controller`): `Promise`\<[`RuleViolation`](../../../api-shared/schedule-validation/types/type-aliases/RuleViolation.md)[]\>

Defined in: [ui/src/api-server/schedule-validation.ts:199](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/schedule-validation.ts#L199)

Every rule, in order — for callers that want the whole report at once (the CLI).

## Parameters

### source

[`ScheduleSource`](../type-aliases/ScheduleSource.md)

### controller

[`DatabaseController`](../../mongo-db-controller/classes/DatabaseController.md)

## Returns

`Promise`\<[`RuleViolation`](../../../api-shared/schedule-validation/types/type-aliases/RuleViolation.md)[]\>
