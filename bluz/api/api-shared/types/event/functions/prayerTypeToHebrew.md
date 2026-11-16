[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / prayerTypeToHebrew

# Function: prayerTypeToHebrew()

> **prayerTypeToHebrew**(`prayerType`): `string`

Defined in: [ui/src/api-shared/types/event.ts:285](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-shared/types/event.ts#L285)

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
