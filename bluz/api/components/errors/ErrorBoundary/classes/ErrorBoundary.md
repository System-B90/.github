[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/errors/ErrorBoundary](../index.md) / ErrorBoundary

# Class: ErrorBoundary

Defined in: [ui/src/components/errors/ErrorBoundary.tsx:27](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/errors/ErrorBoundary.tsx#L27)

React render-phase errors escape the notistack path entirely: a throw
unmounts the tree holding `SnackbarProvider`, so nothing is left to show a
toast. This is the only mechanism that contains such a throw, so it is
placed around each independently-failing subtree (a single event tile, the
calendar, the gantt) rather than once at the root.

Next.js `error.tsx` covers the same class of failure but only at segment
granularity — it replaces the whole page.

## Extends

- `Component`\<[`ErrorBoundaryProps`](../type-aliases/ErrorBoundaryProps.md), `ErrorBoundaryState`\>

## Constructors

### Constructor

> **new ErrorBoundary**(`props`): `ErrorBoundary`

Defined in: node\_modules/@types/react/index.d.ts:958

#### Parameters

##### props

[`ErrorBoundaryProps`](../type-aliases/ErrorBoundaryProps.md)

#### Returns

`ErrorBoundary`

#### Inherited from

`React.Component< ErrorBoundaryProps, ErrorBoundaryState >.constructor`

### Constructor

> **new ErrorBoundary**(`props`, `context`): `ErrorBoundary`

Defined in: node\_modules/@types/react/index.d.ts:966

#### Parameters

##### props

[`ErrorBoundaryProps`](../type-aliases/ErrorBoundaryProps.md)

##### context

`any`

value of the parent [Context](https://react.dev/reference/react/Component#context) specified
in `contextType`.

#### Returns

`ErrorBoundary`

#### Inherited from

`React.Component< ErrorBoundaryProps, ErrorBoundaryState >.constructor`

## Properties

### state

> **state**: `ErrorBoundaryState`

Defined in: [ui/src/components/errors/ErrorBoundary.tsx:31](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/errors/ErrorBoundary.tsx#L31)

#### Overrides

`React.Component.state`

## Methods

### componentDidCatch()

> **componentDidCatch**(`error`, `info`): `void`

Defined in: [ui/src/components/errors/ErrorBoundary.tsx:37](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/errors/ErrorBoundary.tsx#L37)

Catches exceptions generated in descendant components. Unhandled exceptions will cause
the entire component tree to unmount.

#### Parameters

##### error

`Error`

##### info

`ErrorInfo`

#### Returns

`void`

#### Overrides

`React.Component.componentDidCatch`

***

### render()

> **render**(): `ReactNode`

Defined in: [ui/src/components/errors/ErrorBoundary.tsx:47](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/errors/ErrorBoundary.tsx#L47)

#### Returns

`ReactNode`

#### Overrides

`React.Component.render`

***

### getDerivedStateFromError()

> `static` **getDerivedStateFromError**(`error`): `ErrorBoundaryState`

Defined in: [ui/src/components/errors/ErrorBoundary.tsx:33](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/errors/ErrorBoundary.tsx#L33)

#### Parameters

##### error

`Error`

#### Returns

`ErrorBoundaryState`
