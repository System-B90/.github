[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / prayerTypeToHebrew

# Function: prayerTypeToHebrew()

> **prayerTypeToHebrew**(`prayerType`): `string`

Defined in: [ui/src/api-shared/types/event.ts:256](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/event.ts#L256)

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
