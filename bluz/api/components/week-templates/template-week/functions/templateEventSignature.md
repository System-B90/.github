[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/week-templates/template-week](../index.md) / templateEventSignature

# Function: templateEventSignature()

> **templateEventSignature**(`event`): `string`

Defined in: [ui/src/components/week-templates/template-week.ts:40](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/week-templates/template-week.ts#L40)

What saving a template event would store, as a comparable string. Times
count by weekday and clock only, so showing the template in another week
is not a change. Every other stored field counts: a template keeps the
whole event, rooms, instructors and notes included.

## Parameters

### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

## Returns

`string`
