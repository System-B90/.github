[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/outsider-settings/OutsiderFormCard](../index.md) / OutsiderFormCardProps

# Type Alias: OutsiderFormCardProps

> **OutsiderFormCardProps** = `Omit`\<[`FormCardBaseProps`](../../../common/FormCard/type-aliases/FormCardBaseProps.md)\<[`Outsider`](../../../../../../../api-shared/types/outsider/type-aliases/Outsider.md)\>, `"selectedEntity"`\> & `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/outsider-settings/OutsiderFormCard.tsx:10](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/settings-dialog/tabs/global/outsider-settings/OutsiderFormCard.tsx#L10)

## Type Declaration

### setValue

> **setValue**: \<`TKey`\>(`key`, `value`) => `void`

#### Type Parameters

##### TKey

`TKey` *extends* keyof [`OutsiderValues`](../../values/type-aliases/OutsiderValues.md)

#### Parameters

##### key

`TKey`

##### value

[`OutsiderValues`](../../values/type-aliases/OutsiderValues.md)\[`TKey`\]

#### Returns

`void`

### values

> **values**: [`OutsiderValues`](../../values/type-aliases/OutsiderValues.md)
