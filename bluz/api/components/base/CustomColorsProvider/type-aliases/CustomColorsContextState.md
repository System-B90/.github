[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/CustomColorsProvider](../index.md) / CustomColorsContextState

# Type Alias: CustomColorsContextState

> **CustomColorsContextState** = `object`

Defined in: [ui/src/components/base/CustomColorsProvider.tsx:26](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CustomColorsProvider.tsx#L26)

## Properties

### addCustomColor

> **addCustomColor**: (`colorData`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/base/CustomColorsProvider.tsx:34](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CustomColorsProvider.tsx#L34)

#### Parameters

##### colorData

`Omit`\<[`CustomColor`](../../../../api-shared/types/custom-color/type-aliases/CustomColor.md), `"id"`\>

#### Returns

`Promise`\<`boolean`\>

***

### customColors

> **customColors**: [`CustomColor`](../../../../api-shared/types/custom-color/type-aliases/CustomColor.md)[]

Defined in: [ui/src/components/base/CustomColorsProvider.tsx:28](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CustomColorsProvider.tsx#L28)

***

### default

> **default**: `boolean`

Defined in: [ui/src/components/base/CustomColorsProvider.tsx:27](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CustomColorsProvider.tsx#L27)

***

### deleteCustomColor

> **deleteCustomColor**: (`colorId`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/base/CustomColorsProvider.tsx:36](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CustomColorsProvider.tsx#L36)

#### Parameters

##### colorId

`string`

#### Returns

`Promise`\<`boolean`\>

***

### getCustomColor

> **getCustomColor**: (`id`) => [`CustomColor`](../../../../api-shared/types/custom-color/type-aliases/CustomColor.md) \| `null`

Defined in: [ui/src/components/base/CustomColorsProvider.tsx:30](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CustomColorsProvider.tsx#L30)

#### Parameters

##### id

`string`

#### Returns

[`CustomColor`](../../../../api-shared/types/custom-color/type-aliases/CustomColor.md) \| `null`

***

### isLoading

> **isLoading**: `boolean`

Defined in: [ui/src/components/base/CustomColorsProvider.tsx:29](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CustomColorsProvider.tsx#L29)

***

### updateCustomColor

> **updateCustomColor**: (`color`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/base/CustomColorsProvider.tsx:35](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CustomColorsProvider.tsx#L35)

#### Parameters

##### color

[`CustomColor`](../../../../api-shared/types/custom-color/type-aliases/CustomColor.md)

#### Returns

`Promise`\<`boolean`\>
