[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/SaveStatus](../index.md) / useSaveStatus

# Function: useSaveStatus()

> **useSaveStatus**(): `object`

Defined in: [ui/src/components/base/SaveStatus.tsx:15](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/base/SaveStatus.tsx#L15)

Tracks the autosaves of a save-on-blur form (#836): `track(promise)` flips
to "saving", then "saved" or "error". Overlapping saves resolve in order —
only the latest one decides the shown status.

## Returns

`object`

### reset

> **reset**: () => `void`

#### Returns

`void`

### status

> **status**: [`SaveStatus`](../type-aliases/SaveStatus.md)

### track

> **track**: \<`T`\>(`save`) => `Promise`\<`T`\>

#### Type Parameters

##### T

`T`

#### Parameters

##### save

`Promise`\<`T`\>

#### Returns

`Promise`\<`T`\>
