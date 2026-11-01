[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/settings/hive-integration](../index.md) / hiveCalendarFileError

# Function: hiveCalendarFileError()

> **hiveCalendarFileError**(`value`): `string` \| `null`

Defined in: [ui/src/api-shared/types/settings/hive-integration.ts:74](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/settings/hive-integration.ts#L74)

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
