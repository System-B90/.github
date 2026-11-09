[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventHasSubject

# Function: eventHasSubject()

> **eventHasSubject**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:170](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/event.ts#L170)

Checks if a specific event type is associated with an academic subject.

## Parameters

### type

[`EventType`](../enumerations/EventType.md)

The EventType to check.

## Returns

`boolean`

true if the event type requires a subject, false otherwise.

## Example

```typescript
if (eventHasSubject(event.type)) {
  // Render subject and module fields
}
```
