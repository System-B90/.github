[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/IterationProvider](../index.md) / useActiveIterationHiveUrl

# Function: useActiveIterationHiveUrl()

> **useActiveIterationHiveUrl**(): `string` \| `undefined`

Defined in: [ui/src/components/base/IterationProvider.tsx:348](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/base/IterationProvider.tsx#L348)

The Hive instance backing the currently viewed iteration — each iteration
runs against its own Hive, so a hard-coded/env-default base URL would link
a past iteration's data into the wrong instance.

## Returns

`string` \| `undefined`
