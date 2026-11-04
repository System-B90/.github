[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / getPresentInstructors

# Function: getPresentInstructors()

## Call Signature

> **getPresentInstructors**(`event`): `number`[]

Defined in: [ui/src/api-shared/types/event.ts:296](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types/event.ts#L296)

Compiles a unique list of instructor and lecturer IDs present at an event.

### Parameters

#### event

`Pick`\<[`Event`](../type-aliases/Event.md), `"instructors"` \| `"lecturers"`\>

The Event object.

### Returns

`number`[]

Array of unique PersonIds present at the event.

### Example

```typescript
const attendees = getPresentInstructors(event, true);
```

## Call Signature

> **getPresentInstructors**(`event`, `includeOutsiders`): [`PersonId`](../type-aliases/PersonId.md)[]

Defined in: [ui/src/api-shared/types/event.ts:299](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types/event.ts#L299)

Compiles a unique list of instructor and lecturer IDs present at an event.

### Parameters

#### event

`Pick`\<[`Event`](../type-aliases/Event.md), `"instructors"` \| `"lecturers"`\>

The Event object.

#### includeOutsiders

`boolean`

Optional flag to include "איש חוץ" string marker in the return list.

### Returns

[`PersonId`](../type-aliases/PersonId.md)[]

Array of unique PersonIds present at the event.

### Example

```typescript
const attendees = getPresentInstructors(event, true);
```
