[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/IterationProvider](../index.md) / IterationScopeState

# Type Alias: IterationScopeState

> **IterationScopeState** = `object`

Defined in: [ui/src/components/base/IterationProvider.tsx:28](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/IterationProvider.tsx#L28)

## Properties

### currentIterationId

> **currentIterationId**: [`IterationId`](../../../../api-shared/types/iteration/type-aliases/IterationId.md) \| `undefined`

Defined in: [ui/src/components/base/IterationProvider.tsx:37](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/IterationProvider.tsx#L37)

Id of the current (writable) run, once `iterations` has loaded.

***

### isReadOnlyIteration

> **isReadOnlyIteration**: `boolean`

Defined in: [ui/src/components/base/IterationProvider.tsx:33](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/IterationProvider.tsx#L33)

True while viewing a past iteration — every write route rejects it.

***

### iterationId

> **iterationId**: [`IterationId`](../../../../api-shared/types/iteration/type-aliases/IterationId.md) \| `undefined`

Defined in: [ui/src/components/base/IterationProvider.tsx:30](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/IterationProvider.tsx#L30)

Active iteration. `undefined` ⇒ the current (writable) run.

***

### iterations

> **iterations**: [`Iteration`](../../../../api-shared/types/iteration/type-aliases/Iteration.md)[]

Defined in: [ui/src/components/base/IterationProvider.tsx:35](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/IterationProvider.tsx#L35)

All registered iterations, for pickers like `IterationSelector`.

***

### setIterationId

> **setIterationId**: `Dispatch`\<`SetStateAction`\<[`IterationId`](../../../../api-shared/types/iteration/type-aliases/IterationId.md) \| `undefined`\>\>

Defined in: [ui/src/components/base/IterationProvider.tsx:31](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/IterationProvider.tsx#L31)
