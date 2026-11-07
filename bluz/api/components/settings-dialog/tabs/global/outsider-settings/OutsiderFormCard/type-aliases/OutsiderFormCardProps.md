[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/outsider-settings/OutsiderFormCard](../index.md) / OutsiderFormCardProps

# Type Alias: OutsiderFormCardProps

> **OutsiderFormCardProps** = `Omit`\<[`FormCardBaseProps`](../../../common/FormCard/type-aliases/FormCardBaseProps.md)\<[`Outsider`](../../../../../../../api-shared/types/outsider/type-aliases/Outsider.md)\>, `"selectedEntity"`\> & `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/outsider-settings/OutsiderFormCard.tsx:11](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/settings-dialog/tabs/global/outsider-settings/OutsiderFormCard.tsx#L11)

## Type Declaration

### errors

> **errors**: [`FieldErrors`](../../../common/UseEntityForm/type-aliases/FieldErrors.md)\<[`OutsiderValues`](../../values/type-aliases/OutsiderValues.md)\>

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
