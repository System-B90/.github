[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/unavailability](../index.md) / unavailabilityFixedFields

# Function: unavailabilityFixedFields()

> **unavailabilityFixedFields**(): `Pick`\<[`Event`](../../types/event/type-aliases/Event.md), `"courses"` \| `"fake"` \| `"hidden"` \| `"hiveLesson"` \| `"hiveModule"` \| `"lecturers"` \| `"locked"` \| `"personalTalk"` \| `"required"` \| `"rooms"` \| `"splitAcrossBreaks"` \| `"subject"`\>

Defined in: [ui/src/api-shared/unavailability.ts:42](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/unavailability.ts#L42)

The fields an unavailability is pinned to: the pseudo-room, always hidden
from students, and none of a lesson's attributes. Applied by the client
event factory and again by the server on every write, so neither a stale
client nor a hand-made API call can expose one to students.

## Returns

`Pick`\<[`Event`](../../types/event/type-aliases/Event.md), `"courses"` \| `"fake"` \| `"hidden"` \| `"hiveLesson"` \| `"hiveModule"` \| `"lecturers"` \| `"locked"` \| `"personalTalk"` \| `"required"` \| `"rooms"` \| `"splitAcrossBreaks"` \| `"subject"`\>
