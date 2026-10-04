[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/CustomColorsProvider](../index.md) / CustomColorsContextState

# Type Alias: CustomColorsContextState

> **CustomColorsContextState** = `object`

Defined in: [ui/src/components/base/CustomColorsProvider.tsx:27](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/base/CustomColorsProvider.tsx#L27)

## Properties

### addCustomColor

> **addCustomColor**: (`colorData`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/base/CustomColorsProvider.tsx:35](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/base/CustomColorsProvider.tsx#L35)

#### Parameters

##### colorData

`Omit`\<[`CustomColor`](../../../../api-shared/types/custom-color/type-aliases/CustomColor.md), `"id"`\>

#### Returns

`Promise`\<`boolean`\>

***

### customColors

> **customColors**: [`CustomColor`](../../../../api-shared/types/custom-color/type-aliases/CustomColor.md)[]

Defined in: [ui/src/components/base/CustomColorsProvider.tsx:29](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/base/CustomColorsProvider.tsx#L29)

***

### default

> **default**: `boolean`

Defined in: [ui/src/components/base/CustomColorsProvider.tsx:28](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/base/CustomColorsProvider.tsx#L28)

***

### deleteCustomColor

> **deleteCustomColor**: (`colorId`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/base/CustomColorsProvider.tsx:37](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/base/CustomColorsProvider.tsx#L37)

#### Parameters

##### colorId

`string`

#### Returns

`Promise`\<`boolean`\>

***

### getCustomColor

> **getCustomColor**: (`id`) => [`CustomColor`](../../../../api-shared/types/custom-color/type-aliases/CustomColor.md) \| `null`

Defined in: [ui/src/components/base/CustomColorsProvider.tsx:31](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/base/CustomColorsProvider.tsx#L31)

#### Parameters

##### id

`string`

#### Returns

[`CustomColor`](../../../../api-shared/types/custom-color/type-aliases/CustomColor.md) \| `null`

***

### isLoading

> **isLoading**: `boolean`

Defined in: [ui/src/components/base/CustomColorsProvider.tsx:30](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/base/CustomColorsProvider.tsx#L30)

***

### updateCustomColor

> **updateCustomColor**: (`color`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/base/CustomColorsProvider.tsx:36](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/base/CustomColorsProvider.tsx#L36)

#### Parameters

##### color

[`CustomColor`](../../../../api-shared/types/custom-color/type-aliases/CustomColor.md)

#### Returns

`Promise`\<`boolean`\>
