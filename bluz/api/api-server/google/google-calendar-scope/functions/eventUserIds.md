[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-scope](../index.md) / eventUserIds

# Function: eventUserIds()

> **eventUserIds**(`event`): `Set`\<`string`\>

Defined in: [ui/src/api-server/google/google-calendar-scope.ts:16](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-server/google/google-calendar-scope.ts#L16)

Bluz user ids (as strings) assigned to the event as instructor/lecturer.

## Parameters

### event

`Pick`\<[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md), `"instructors"` \| `"lecturers"`\>

## Returns

`Set`\<`string`\>
