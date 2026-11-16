[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/student-view/no-overlap-layout](../index.md) / LaneKey

# Type Alias: LaneKey\<TEvent\>

> **LaneKey**\<`TEvent`\> = (`event`) => `null` \| `string`

Defined in: [ui/src/components/student-view/no-overlap-layout.ts:90](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/student-view/no-overlap-layout.ts#L90)

Groups tiles that must share a column band (#988): every tile with the same
non-null key gets the same column(s) and the same width within a cluster.
Null keys pack freely, as before.

## Type Parameters

### TEvent

`TEvent`

## Parameters

### event

`TEvent`

## Returns

`null` \| `string`
