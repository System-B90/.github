[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / prayerTypeToHebrew

# Function: prayerTypeToHebrew()

> **prayerTypeToHebrew**(`prayerType`): `string`

Defined in: [ui/src/api-shared/types/event.ts:260](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/types/event.ts#L260)

Translates a prayer type enum value to its displayable Hebrew name.

## Parameters

### prayerType

[`PrayerType`](../enumerations/PrayerType.md)

The PrayerType enum value.

## Returns

`string`

Hebrew string representing the prayer name.

## Example

```typescript
const label = prayerTypeToHebrew(PrayerType.SHACHARIT); // "שחרית"
```
