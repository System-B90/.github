[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/IterationProvider](../index.md) / useActiveIterationHiveUrl

# Function: useActiveIterationHiveUrl()

> **useActiveIterationHiveUrl**(): `string` \| `undefined`

Defined in: [ui/src/components/base/IterationProvider.tsx:348](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/IterationProvider.tsx#L348)

The Hive instance backing the currently viewed iteration — each iteration
runs against its own Hive, so a hard-coded/env-default base URL would link
a past iteration's data into the wrong instance.

## Returns

`string` \| `undefined`
