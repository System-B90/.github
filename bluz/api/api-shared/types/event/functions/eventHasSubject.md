[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventHasSubject

# Function: eventHasSubject()

> **eventHasSubject**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:171](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/event.ts#L171)

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
