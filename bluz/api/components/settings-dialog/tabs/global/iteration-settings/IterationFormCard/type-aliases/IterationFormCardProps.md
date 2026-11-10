[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/iteration-settings/IterationFormCard](../index.md) / IterationFormCardProps

# Type Alias: IterationFormCardProps

> **IterationFormCardProps** = `Omit`\<[`FormCardBaseProps`](../../../common/FormCard/type-aliases/FormCardBaseProps.md)\<[`Iteration`](../../../../../../../api-shared/types/iteration/type-aliases/Iteration.md)\>, `"selectedEntity"`\> & `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/iteration-settings/IterationFormCard.tsx:16](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/settings-dialog/tabs/global/iteration-settings/IterationFormCard.tsx#L16)

## Type Declaration

### errors

> **errors**: [`FieldErrors`](../../../common/UseEntityForm/type-aliases/FieldErrors.md)\<[`IterationValues`](../../values/type-aliases/IterationValues.md)\>

### handleDelete

> **handleDelete**: (`iteration`) => `void`

#### Parameters

##### iteration

[`Iteration`](../../../../../../../api-shared/types/iteration/type-aliases/Iteration.md)

#### Returns

`void`

### handleSyncHive

> **handleSyncHive**: (`iteration`) => `void`

#### Parameters

##### iteration

[`Iteration`](../../../../../../../api-shared/types/iteration/type-aliases/Iteration.md)

#### Returns

`void`

### isDeleting

> **isDeleting**: `boolean`

### isSubmitting

> **isSubmitting**: `boolean`

### isSyncingHive

> **isSyncingHive**: `boolean`

### setValue

> **setValue**: \<`TKey`\>(`key`, `value`) => `void`

#### Type Parameters

##### TKey

`TKey` *extends* keyof [`IterationValues`](../../values/type-aliases/IterationValues.md)

#### Parameters

##### key

`TKey`

##### value

[`IterationValues`](../../values/type-aliases/IterationValues.md)\[`TKey`\]

#### Returns

`void`

### usage

> **usage**: [`IterationUsage`](../../../../../../../api-shared/types/iteration/type-aliases/IterationUsage.md) \| `null`

Null while the usage probe is still in flight.

### values

> **values**: [`IterationValues`](../../values/type-aliases/IterationValues.md)
