[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/hive-load-failure](../index.md) / reportHiveLoadFailure

# Function: reportHiveLoadFailure()

> **reportHiveLoadFailure**(`resource`, `error`, `retry`): `void`

Defined in: [ui/src/components/base/hive-load-failure.tsx:114](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/base/hive-load-failure.tsx#L114)

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
