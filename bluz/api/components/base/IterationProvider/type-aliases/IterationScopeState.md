[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/IterationProvider](../index.md) / IterationScopeState

# Type Alias: IterationScopeState

> **IterationScopeState** = `object`

Defined in: [ui/src/components/base/IterationProvider.tsx:54](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/IterationProvider.tsx#L54)

## Properties

### currentIterationId

> **currentIterationId**: [`IterationId`](../../../../api-shared/types/iteration/type-aliases/IterationId.md) \| `undefined`

Defined in: [ui/src/components/base/IterationProvider.tsx:70](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/IterationProvider.tsx#L70)

Id of the current (writable) run, once `iterations` has loaded.

***

### isReadOnlyIteration

> **isReadOnlyIteration**: `boolean`

Defined in: [ui/src/components/base/IterationProvider.tsx:62](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/IterationProvider.tsx#L62)

True while viewing a past iteration, or always for a view-only
(Checker) user — every write route rejects both.

***

### iterationId

> **iterationId**: [`IterationId`](../../../../api-shared/types/iteration/type-aliases/IterationId.md) \| `undefined`

Defined in: [ui/src/components/base/IterationProvider.tsx:56](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/IterationProvider.tsx#L56)

Active iteration. `undefined` ⇒ the current (writable) run.

***

### iterations

> **iterations**: [`Iteration`](../../../../api-shared/types/iteration/type-aliases/Iteration.md)[]

Defined in: [ui/src/components/base/IterationProvider.tsx:68](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/IterationProvider.tsx#L68)

All registered iterations, for pickers like `IterationSelector`.

***

### readOnlyHint

> **readOnlyHint**: `string`

Defined in: [ui/src/components/base/IterationProvider.tsx:64](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/IterationProvider.tsx#L64)

Tooltip for a write control disabled by `isReadOnlyIteration`.

***

### readOnlyMessage

> **readOnlyMessage**: `string`

Defined in: [ui/src/components/base/IterationProvider.tsx:66](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/IterationProvider.tsx#L66)

Refusal text for a write attempted under `isReadOnlyIteration`.

***

### setIterationId

> **setIterationId**: `Dispatch`\<`SetStateAction`\<[`IterationId`](../../../../api-shared/types/iteration/type-aliases/IterationId.md) \| `undefined`\>\>

Defined in: [ui/src/components/base/IterationProvider.tsx:57](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/IterationProvider.tsx#L57)
