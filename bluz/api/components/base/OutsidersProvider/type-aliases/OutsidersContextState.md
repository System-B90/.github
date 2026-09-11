[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/OutsidersProvider](../index.md) / OutsidersContextState

# Type Alias: OutsidersContextState

> **OutsidersContextState** = `object`

Defined in: [ui/src/components/base/OutsidersProvider.tsx:14](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OutsidersProvider.tsx#L14)

## Properties

### addOutsider

> **addOutsider**: (`outsiderData`) => `Promise`\<`void`\>

Defined in: [ui/src/components/base/OutsidersProvider.tsx:19](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OutsidersProvider.tsx#L19)

#### Parameters

##### outsiderData

`Omit`\<[`Outsider`](../../../../api-shared/types/outsider/type-aliases/Outsider.md), `"id"`\>

#### Returns

`Promise`\<`void`\>

***

### default

> **default**: `boolean`

Defined in: [ui/src/components/base/OutsidersProvider.tsx:15](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OutsidersProvider.tsx#L15)

***

### deleteOutsider

> **deleteOutsider**: (`outsiderId`) => `Promise`\<`void`\>

Defined in: [ui/src/components/base/OutsidersProvider.tsx:21](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OutsidersProvider.tsx#L21)

#### Parameters

##### outsiderId

`string`

#### Returns

`Promise`\<`void`\>

***

### getOutsider

> **getOutsider**: (`id`) => `null` \| [`Outsider`](../../../../api-shared/types/outsider/type-aliases/Outsider.md)

Defined in: [ui/src/components/base/OutsidersProvider.tsx:18](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OutsidersProvider.tsx#L18)

#### Parameters

##### id

`string`

#### Returns

`null` \| [`Outsider`](../../../../api-shared/types/outsider/type-aliases/Outsider.md)

***

### isLoading

> **isLoading**: `boolean`

Defined in: [ui/src/components/base/OutsidersProvider.tsx:17](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OutsidersProvider.tsx#L17)

***

### outsiders

> **outsiders**: [`Outsider`](../../../../api-shared/types/outsider/type-aliases/Outsider.md)[]

Defined in: [ui/src/components/base/OutsidersProvider.tsx:16](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OutsidersProvider.tsx#L16)

***

### updateOutsider

> **updateOutsider**: (`outsider`) => `Promise`\<`void`\>

Defined in: [ui/src/components/base/OutsidersProvider.tsx:20](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/OutsidersProvider.tsx#L20)

#### Parameters

##### outsider

[`Outsider`](../../../../api-shared/types/outsider/type-aliases/Outsider.md)

#### Returns

`Promise`\<`void`\>
