[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/onboarding/core/anchors](../index.md) / AnchorRegistry

# Class: AnchorRegistry

Defined in: [ui/src/components/onboarding/core/anchors.ts:13](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/core/anchors.ts#L13)

The live map of anchor id → mounted element.

Components register themselves as they mount (`useTourAnchor`), so a tour can
ask "where is `gantt.tabs` right now?" without ever touching a selector or
reaching across the component tree. Registering an id that is already taken
wins — the newest mount is the one on screen.

## Constructors

### Constructor

> **new AnchorRegistry**(): `AnchorRegistry`

#### Returns

`AnchorRegistry`

## Methods

### get()

> **get**(`id`): `HTMLElement` \| `undefined`

Defined in: [ui/src/components/onboarding/core/anchors.ts:31](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/core/anchors.ts#L31)

#### Parameters

##### id

`string`

#### Returns

`HTMLElement` \| `undefined`

***

### has()

> **has**(`id`): `boolean`

Defined in: [ui/src/components/onboarding/core/anchors.ts:44](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/core/anchors.ts#L44)

#### Parameters

##### id

`string`

#### Returns

`boolean`

***

### register()

> **register**(`id`, `element`): () => `void`

Defined in: [ui/src/components/onboarding/core/anchors.ts:18](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/core/anchors.ts#L18)

Returns the un-register callback, so it can be a ref cleanup directly.

#### Parameters

##### id

`string`

##### element

`HTMLElement`

#### Returns

() => `void`

***

### subscribe()

> **subscribe**(`listener`): () => `void`

Defined in: [ui/src/components/onboarding/core/anchors.ts:48](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/core/anchors.ts#L48)

#### Parameters

##### listener

`AnchorListener`

#### Returns

() => `void`
