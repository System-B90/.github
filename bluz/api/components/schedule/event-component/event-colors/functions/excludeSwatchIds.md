[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-component/event-colors](../index.md) / excludeSwatchIds

# Function: excludeSwatchIds()

> **excludeSwatchIds**\<`T`\>(`swatches`, `excludeIds`): `T`[]

Defined in: [ui/src/components/schedule/event-component/event-colors.ts:97](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/event-component/event-colors.ts#L97)

Filters out swatches whose id is already present in `excludeIds` - used to
keep a recently-used color from being listed twice when it's also a
subject or custom color shown in its own group.

## Type Parameters

### T

`T` *extends* `object`

## Parameters

### swatches

`T`[]

### excludeIds

`Iterable`\<`string`\>

## Returns

`T`[]
