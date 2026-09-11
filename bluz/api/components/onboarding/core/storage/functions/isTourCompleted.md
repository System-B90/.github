[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/onboarding/core/storage](../index.md) / isTourCompleted

# Function: isTourCompleted()

> **isTourCompleted**(`completions`, `tour`): `boolean`

Defined in: [ui/src/components/onboarding/core/storage.ts:67](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/core/storage.ts#L67)

A tour counts as done only while its recorded version still matches. Bumping
`Tour.version` is therefore how a materially rewritten tour is shown again to
users who already saw the old one.

## Parameters

### completions

[`CompletionMap`](../type-aliases/CompletionMap.md)

### tour

`Pick`\<[`Tour`](../../../types/type-aliases/Tour.md), `"id"` \| `"version"`\>

## Returns

`boolean`
