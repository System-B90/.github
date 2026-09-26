[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/IterationProvider](../index.md) / IterationScopeState

# Type Alias: IterationScopeState

> **IterationScopeState** = `object`

Defined in: [ui/src/components/base/IterationProvider.tsx:36](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/IterationProvider.tsx#L36)

## Properties

### currentIterationId

> **currentIterationId**: [`IterationId`](../../../../api-shared/types/iteration/type-aliases/IterationId.md) \| `undefined`

Defined in: [ui/src/components/base/IterationProvider.tsx:45](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/IterationProvider.tsx#L45)

Id of the current (writable) run, once `iterations` has loaded.

***

### isReadOnlyIteration

> **isReadOnlyIteration**: `boolean`

Defined in: [ui/src/components/base/IterationProvider.tsx:41](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/IterationProvider.tsx#L41)

True while viewing a past iteration — every write route rejects it.

***

### iterationId

> **iterationId**: [`IterationId`](../../../../api-shared/types/iteration/type-aliases/IterationId.md) \| `undefined`

Defined in: [ui/src/components/base/IterationProvider.tsx:38](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/IterationProvider.tsx#L38)

Active iteration. `undefined` ⇒ the current (writable) run.

***

### iterations

> **iterations**: [`Iteration`](../../../../api-shared/types/iteration/type-aliases/Iteration.md)[]

Defined in: [ui/src/components/base/IterationProvider.tsx:43](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/IterationProvider.tsx#L43)

All registered iterations, for pickers like `IterationSelector`.

***

### setIterationId

> **setIterationId**: `Dispatch`\<`SetStateAction`\<[`IterationId`](../../../../api-shared/types/iteration/type-aliases/IterationId.md) \| `undefined`\>\>

Defined in: [ui/src/components/base/IterationProvider.tsx:39](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/IterationProvider.tsx#L39)
