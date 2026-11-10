[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/settings/hive-integration](../index.md) / hiveCalendarFileError

# Function: hiveCalendarFileError()

> **hiveCalendarFileError**(`value`): `string` \| `null`

Defined in: [ui/src/api-shared/types/settings/hive-integration.ts:74](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/settings/hive-integration.ts#L74)

Why a calendar file path cannot be used, in Hebrew, or null when it can.

## Parameters

### value

`unknown`

The path as typed, relative to the shared calendar directory.

## Returns

`string` \| `null`

The validation message, or null.

## Example

```typescript
hiveCalendarFileError("bluz/Calendar.ics"); // null
hiveCalendarFileError("../etc/passwd"); // "…"
```
