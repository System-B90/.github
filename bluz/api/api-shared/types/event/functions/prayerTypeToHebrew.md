[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / prayerTypeToHebrew

# Function: prayerTypeToHebrew()

> **prayerTypeToHebrew**(`prayerType`): `string`

Defined in: [ui/src/api-shared/types/event.ts:284](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/event.ts#L284)

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
