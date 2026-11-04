[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/EntitySelect](../index.md) / EntitySelectProps

# Type Alias: EntitySelectProps\<TId\>

> **EntitySelectProps**\<`TId`\> = `object` & `Omit`\<`FormControlProps`, `"onChange"`\>

Defined in: [ui/src/components/base/EntitySelect.tsx:20](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/base/EntitySelect.tsx#L20)

## Type Declaration

### allowEmpty?

> `optional` **allowEmpty?**: `boolean`

Render a leading empty option so the user can clear the choice.

### autoSelectSole?

> `optional` **autoSelectSole?**: `boolean`

Pick the option automatically when it is the only one and nothing is
selected. Fires once per sole option, so clearing it sticks.

### disableWhenEmpty?

> `optional` **disableWhenEmpty?**: `boolean`

Disable the control when there is nothing to pick. Defaults to true.

### emptyLabel?

> `optional` **emptyLabel?**: `string`

Label for the empty option.

### endAdornment?

> `optional` **endAdornment?**: `ReactNode`

Rendered inside the field, before the dropdown arrow.

### label

> **label**: `string`

Field label.

### onChange

> **onChange**: (`id`) => `void`

Fired with the picked entity id, or null when cleared.

#### Parameters

##### id

`null` \| `TId`

#### Returns

`void`

### options

> **options**: `ReadonlyArray`\<[`NamedEntity`](NamedEntity.md)\<`TId`\>\>

Options to offer. Sorted by name (Hebrew collation) internally.

### parseValue

> **parseValue**: (`raw`) => `TId`

Coerce the raw `<select>` value back to the id type.

#### Parameters

##### raw

`string`

#### Returns

`TId`

### searchable?

> `optional` **searchable?**: `boolean`

Top the menu with a type-to-filter search box.

### searchPlaceholder?

> `optional` **searchPlaceholder?**: `string`

Placeholder for the search box.

### value

> **value**: `null` \| `TId`

Selected entity id (controlled). Use null for no selection.

## Type Parameters

### TId

`TId` *extends* `number` \| `string`
