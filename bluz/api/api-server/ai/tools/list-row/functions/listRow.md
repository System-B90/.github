[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/list-row](../index.md) / listRow

# Function: listRow()

> **listRow**(`summary`, `fields`): `Partial`\<[`AiEventSummary`](../../calendar/type-aliases/AiEventSummary.md)\>

Defined in: [ui/src/api-server/ai/tools/list-row.ts:46](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/ai/tools/list-row.ts#L46)

One list row: the base columns plus the requested extras, minus empty
values. A week of meals would otherwise repeat the same `[]` and `false`
per row and crowd the real rows out of the result cap.

## Parameters

### summary

#### color

`string` \| `null` = `...`

#### courses

`string`[] = `event.courses`

#### endTime

`string` = `...`

#### fake

`boolean` = `...`

#### hidden

`boolean` = `event.hidden`

#### id

`string` = `event.id`

#### instructors

`number`[] = `event.instructors`

#### lecturers

[`PersonId`](../../../../../api-shared/types/event/type-aliases/PersonId.md)[] \| `undefined` = `event.lecturers`

#### locked

`boolean` = `event.locked`

#### name

`string` = `event.name`

#### notes

`string` = `event.notes`

#### rooms

[`ResolvableRoom`](../../../../../api-shared/types/room/type-aliases/ResolvableRoom.md)[] = `event.rooms`

#### startTime

`string` = `...`

#### type

[`EventType`](../../../../../api-shared/types/event/enumerations/EventType.md) = `event.type`

### fields

(`"type"` \| `"courses"` \| `"rooms"` \| `"instructors"` \| `"lecturers"` \| `"notes"` \| `"locked"` \| `"hidden"` \| `"color"` \| `"fake"`)[]

## Returns

`Partial`\<[`AiEventSummary`](../../calendar/type-aliases/AiEventSummary.md)\>
