[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventTypeToHebrew

# Function: eventTypeToHebrew()

> **eventTypeToHebrew**(`type`): `string`

Defined in: [ui/src/api-shared/types/event.ts:300](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L300)

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
