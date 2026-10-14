[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-preferences](../index.md) / createViewerSetting

# Function: createViewerSetting()

> **createViewerSetting**\<`T`\>(`key`, `defaultValue`, `parse`, `format`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-preferences.ts:4](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-preferences.ts#L4)

A per-viewer value kept in localStorage and shared by every component that reads it.

## Type Parameters

### T

`T`

## Parameters

### key

`string`

### defaultValue

`T`

### parse

(`saved`) => `T`

Stored text → value; null (nothing stored) never reaches it.

### format

(`value`) => `string` \| `null`

Value → stored text; null removes the key.

## Returns

`object`

### get

> **get**: () => `T`

#### Returns

`T`

### set

> **set**: (`next`) => `void`

#### Parameters

##### next

`T`

#### Returns

`void`

### use

> **use**: () => `T`

#### Returns

`T`
