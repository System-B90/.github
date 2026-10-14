[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/external-store](../index.md) / ExternalStore

# Type Alias: ExternalStore\<T\>

> **ExternalStore**\<`T`\> = `object`

Defined in: [ui/src/components/base/external-store.ts:13](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/base/external-store.ts#L13)

A value held outside React state, read through per-consumer selectors.

The schedule grid has hundreds of tiles. State that lives in a context (or
in a component above the calendar) re-renders every one of them whenever it
changes, even when only one tile's answer changed: hover (#924), the drag in
flight and the lock map (#955). A tile that reads through
[useStoreSelector](../functions/useStoreSelector.md) re-renders only when *its* selected value changes.

## Type Parameters

### T

`T`

## Properties

### get

> **get**: () => `T`

Defined in: [ui/src/components/base/external-store.ts:14](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/base/external-store.ts#L14)

#### Returns

`T`

***

### set

> **set**: (`value`) => `void`

Defined in: [ui/src/components/base/external-store.ts:16](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/base/external-store.ts#L16)

No-op (no notification) when `value` is identical to the current one.

#### Parameters

##### value

`T`

#### Returns

`void`

***

### subscribe

> **subscribe**: (`listener`) => () => `void`

Defined in: [ui/src/components/base/external-store.ts:19](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/base/external-store.ts#L19)

#### Parameters

##### listener

() => `void`

#### Returns

() => `void`

***

### update

> **update**: (`fn`) => `void`

Defined in: [ui/src/components/base/external-store.ts:18](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/base/external-store.ts#L18)

Functional update, like a state setter.

#### Parameters

##### fn

(`current`) => `T`

#### Returns

`void`
