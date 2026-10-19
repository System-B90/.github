[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / getPresentInstructors

# Function: getPresentInstructors()

> **getPresentInstructors**(`event`): `number`[]

Defined in: [ui/src/api-shared/types/event.ts:315](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L315)

Compiles a unique list of instructor and lecturer IDs present at an event.

## Parameters

### event

`Pick`\<[`Event`](../type-aliases/Event.md), `"instructors"` \| `"lecturers"`\>

The Event object.

## Returns

`number`[]

Array of unique PersonIds present at the event.

## Example

```typescript
const attendees = getPresentInstructors(event, true);
```
