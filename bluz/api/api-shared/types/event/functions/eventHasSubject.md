[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventHasSubject

# Function: eventHasSubject()

> **eventHasSubject**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:171](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/api-shared/types/event.ts#L171)

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
