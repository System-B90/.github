[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/IterationProvider](../index.md) / useActiveIterationHiveUrl

# Function: useActiveIterationHiveUrl()

> **useActiveIterationHiveUrl**(): `string` \| `undefined`

Defined in: [ui/src/components/base/IterationProvider.tsx:303](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/IterationProvider.tsx#L303)

The Hive instance backing the currently viewed iteration — each iteration
runs against its own Hive, so a hard-coded/env-default base URL would link
a past iteration's data into the wrong instance.

## Returns

`string` \| `undefined`
