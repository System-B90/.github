[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/week-templates/template-week](../index.md) / templateEventSignature

# Function: templateEventSignature()

> **templateEventSignature**(`event`): `string`

Defined in: [ui/src/components/week-templates/template-week.ts:40](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/week-templates/template-week.ts#L40)

What saving a template event would store, as a comparable string. Times
count by weekday and clock only, so showing the template in another week
is not a change. Every other stored field counts: a template keeps the
whole event, rooms, instructors and notes included.

## Parameters

### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

## Returns

`string`
