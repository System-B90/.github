[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/student-view/no-overlap-layout](../index.md) / LaneKey

# Type Alias: LaneKey\<TEvent\>

> **LaneKey**\<`TEvent`\> = (`event`) => `null` \| `string`

Defined in: [ui/src/components/student-view/no-overlap-layout.ts:90](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/student-view/no-overlap-layout.ts#L90)

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
