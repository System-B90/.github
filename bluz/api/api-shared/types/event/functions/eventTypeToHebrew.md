[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventTypeToHebrew

# Function: eventTypeToHebrew()

> **eventTypeToHebrew**(`type`): `string`

Defined in: [ui/src/api-shared/types/event.ts:281](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/types/event.ts#L281)

Returns the displayable Hebrew label for a given EventType.
Since the EventType enum is standardized to Hebrew values, this returns the value itself.

## Parameters

### type

[`EventType`](../enumerations/EventType.md)

The EventType to translate.

## Returns

`string`

The Hebrew display string.

## Example

```typescript
const label = eventTypeToHebrew(event.type); // "הרצאה", "תפילה", etc.
```
