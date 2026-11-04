[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/SelectSearchHeader](../index.md) / useSelectSearch

# Function: useSelectSearch()

> **useSelectSearch**\<`T`\>(`options`, `nameOf`, `isSelected?`): `object`

Defined in: [ui/src/components/base/SelectSearchHeader.tsx:106](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/base/SelectSearchHeader.tsx#L106)

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
