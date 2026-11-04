[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/external-store](../index.md) / useStoreSelector

# Function: useStoreSelector()

> **useStoreSelector**\<`T`, `S`\>(`store`, `selector`): `S`

Defined in: [ui/src/components/base/external-store.ts:49](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/base/external-store.ts#L49)

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
