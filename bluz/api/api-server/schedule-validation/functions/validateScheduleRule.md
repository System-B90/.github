[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/schedule-validation](../index.md) / validateScheduleRule

# Function: validateScheduleRule()

> **validateScheduleRule**(`ruleId`, `source`, `controller`): `Promise`\<[`RuleViolation`](../../../api-shared/schedule-validation/types/type-aliases/RuleViolation.md)[]\>

Defined in: [ui/src/api-server/schedule-validation.ts:186](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/schedule-validation.ts#L186)

Runs one rule's check over the source.

## Parameters

### ruleId

`"R-10"` \| `"R-11"` \| `"R-12"` \| `"R-20"` \| `"R-21"` \| `"R-23"` \| `"R-24"` \| `"R-25"` \| `"R-26"` \| `"R-27"` \| `"R-32"` \| `"R-40"` \| `"R-41"` \| `"R-42"` \| `"R-47"` \| `"R-49b"` \| `"R-49d"` \| `"R-48a"` \| `"R-50"` \| `"R-51"` \| `"R-55"` \| `"R-57"` \| `"R-58"` \| `"R-60"` \| `"R-64"` \| `"R-65"` \| `"R-71"` \| `"R-68"` \| `"R-69"` \| `"R-6A"`

### source

[`ScheduleSource`](../type-aliases/ScheduleSource.md)

### controller

[`DatabaseController`](../../mongo-db-controller/classes/DatabaseController.md)

## Returns

`Promise`\<[`RuleViolation`](../../../api-shared/schedule-validation/types/type-aliases/RuleViolation.md)[]\>
