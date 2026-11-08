[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/SelectSearchHeader](../index.md) / useSelectSearch

# Function: useSelectSearch()

> **useSelectSearch**\<`T`\>(`options`, `nameOf`, `isSelected?`): `object`

Defined in: [ui/src/components/base/SelectSearchHeader.tsx:106](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/base/SelectSearchHeader.tsx#L106)

Query state for a Select topped by `SelectSearchHeader`: the options whose
name matches, plus any selected ones (a single Select blanks a value with
no matching MenuItem, and a multiple one would hide its checkmarks).
Call `reset` from the Select's `onClose`.

## Type Parameters

### T

`T`

## Parameters

### options

readonly `T`[]

### nameOf

(`option`) => `string`

### isSelected?

(`option`) => `boolean`

## Returns

`object`

### query

> **query**: `string`

### reset

> **reset**: () => `void`

#### Returns

`void`

### setQuery

> **setQuery**: `Dispatch`\<`SetStateAction`\<`string`\>\>

### visible

> **visible**: readonly `T`[]
