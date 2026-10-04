[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / getPresentInstructors

# Function: getPresentInstructors()

> **getPresentInstructors**(`event`): `number`[]

Defined in: [ui/src/api-shared/types/event.ts:291](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-shared/types/event.ts#L291)

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
