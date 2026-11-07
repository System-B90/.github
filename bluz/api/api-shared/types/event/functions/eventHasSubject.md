[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventHasSubject

# Function: eventHasSubject()

> **eventHasSubject**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:164](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/types/event.ts#L164)

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
