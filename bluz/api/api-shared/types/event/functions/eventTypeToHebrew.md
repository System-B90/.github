[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventTypeToHebrew

# Function: eventTypeToHebrew()

> **eventTypeToHebrew**(`type`): `string`

Defined in: [ui/src/api-shared/types/event.ts:305](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/event.ts#L305)

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
