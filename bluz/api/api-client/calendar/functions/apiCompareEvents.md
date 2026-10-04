[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar](../index.md) / apiCompareEvents

# Function: apiCompareEvents()

> **apiCompareEvents**(`__namedParameters`): `Promise`\<\{ `a`: [`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]; `b`: [`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]; \}\>

Defined in: [ui/src/api-client/calendar.ts:192](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-client/calendar.ts#L192)

Fetch the events of two iterations over the same date range in one round-trip,
for side-by-side / week comparison views.

## Parameters

### \_\_namedParameters

#### endDate

`Date`

#### iterationA?

`string`

#### iterationB?

`string`

#### startDate

`Date`

## Returns

`Promise`\<\{ `a`: [`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]; `b`: [`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]; \}\>
