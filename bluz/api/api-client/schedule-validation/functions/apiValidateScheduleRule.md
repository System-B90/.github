[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/schedule-validation](../index.md) / apiValidateScheduleRule

# Function: apiValidateScheduleRule()

> **apiValidateScheduleRule**(`ruleId`, `request`, `iterationId?`, `signal?`): `Promise`\<[`RuleValidationResponse`](../../../api-shared/schedule-validation/types/type-aliases/RuleValidationResponse.md)\>

Defined in: [ui/src/api-client/schedule-validation.ts:11](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-client/schedule-validation.ts#L11)

One schedule rule's check over a range, a saved draft or inline events.

## Parameters

### ruleId

`"R-10"` \| `"R-11"` \| `"R-12"` \| `"R-20"` \| `"R-21"` \| `"R-23"` \| `"R-24"` \| `"R-25"` \| `"R-26"` \| `"R-27"` \| `"R-32"` \| `"R-40"` \| `"R-41"` \| `"R-42"` \| `"R-47"` \| `"R-49b"` \| `"R-49d"` \| `"R-48a"` \| `"R-50"` \| `"R-51"` \| `"R-55"` \| `"R-57"` \| `"R-58"` \| `"R-60"` \| `"R-64"` \| `"R-65"` \| `"R-71"` \| `"R-68"` \| `"R-69"` \| `"R-6A"`

### request

[`RuleValidationRequest`](../../../api-shared/schedule-validation/types/type-aliases/RuleValidationRequest.md)

### iterationId?

`string`

### signal?

`AbortSignal`

## Returns

`Promise`\<[`RuleValidationResponse`](../../../api-shared/schedule-validation/types/type-aliases/RuleValidationResponse.md)\>
