[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/hive-load-failure](../index.md) / reportHiveLoadFailure

# Function: reportHiveLoadFailure()

> **reportHiveLoadFailure**(`resource`, `error`, `retry`): `void`

Defined in: [ui/src/components/base/hive-load-failure.tsx:114](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/base/hive-load-failure.tsx#L114)

Report a failed Hive lookup (#823). Failures close together merge into one
toast that says, in plain Hebrew, what the user loses, with a retry action;
the technical error sits behind a `פרטים` toggle.

## Parameters

### resource

`"users"` \| `"subjects"`

### error

`unknown`

### retry

() => `void`

## Returns

`void`
