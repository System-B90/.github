[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/schedule-validation/common](../index.md) / perEvent

# Function: perEvent()

> **perEvent**(`rule`, `summary`, `items`, `context`): [`RuleViolation`](../../types/type-aliases/RuleViolation.md)[]

Defined in: [ui/src/api-shared/schedule-validation/common.ts:214](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/schedule-validation/common.ts#L214)

One violation per offending event, labelled by the event.

## Parameters

### rule

`"R-01"` \| `"R-02"` \| `"R-03"` \| `"R-10"` \| `"R-11"` \| `"R-12"` \| `"R-13"` \| `"R-14"` \| `"R-20"` \| `"R-21"` \| `"R-22"` \| `"R-23"` \| `"R-24"` \| `"R-25"` \| `"R-26"` \| `"R-27"` \| `"R-30"` \| `"R-31"` \| `"R-32"` \| `"R-40"` \| `"R-41"` \| `"R-42"` \| `"R-43"` \| `"R-44"` \| `"R-45"` \| `"R-46"` \| `"R-47"` \| `"R-48"` \| `"R-49a"` \| `"R-49b"` \| `"R-49c"` \| `"R-49d"` \| `"R-49e"` \| `"R-48a"` \| `"R-48b"` \| `"R-48c"` \| `"R-50"` \| `"R-51"` \| `"R-52"` \| `"R-53"` \| `"R-54"` \| `"R-55"` \| `"R-56"` \| `"R-57"` \| `"R-58"` \| `"R-59"` \| `"R-5A"` \| `"R-60"` \| `"R-61"` \| `"R-62"` \| `"R-63"` \| `"R-64"` \| `"R-65"` \| `"R-66"` \| `"R-70"` \| `"R-71"` \| `"R-67"` \| `"R-68"` \| `"R-69"` \| `"R-6A"` \| `"R-80"` \| `"R-81"` \| `"R-82"` \| `"R-83"` \| `"R-84"` \| `"R-85"`

### summary

`string`

### items

readonly [`Timed`](../type-aliases/Timed.md)[]

### context

[`RuleCheckContext`](../../types/type-aliases/RuleCheckContext.md)

## Returns

[`RuleViolation`](../../types/type-aliases/RuleViolation.md)[]
