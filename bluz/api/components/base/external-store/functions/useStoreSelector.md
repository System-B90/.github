[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/external-store](../index.md) / useStoreSelector

# Function: useStoreSelector()

> **useStoreSelector**\<`T`, `S`\>(`store`, `selector`): `S`

Defined in: [ui/src/components/base/external-store.ts:46](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/base/external-store.ts#L46)

Subscribes to `store`, re-rendering only when `selector`'s result changes
(by `Object.is`). The selector must return a primitive or an object that
is already stored, never a fresh one, or it re-renders on every change.

## Type Parameters

### T

`T`

### S

`S`

## Parameters

### store

[`ExternalStore`](../type-aliases/ExternalStore.md)\<`T`\>

### selector

(`value`) => `S`

## Returns

`S`
