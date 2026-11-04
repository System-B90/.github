[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-preferences](../index.md) / createViewerFlag

# Function: createViewerFlag()

> **createViewerFlag**(`key`, `defaultValue`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-preferences.ts:54](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-preferences.ts#L54)

A per-viewer on/off flag kept in localStorage and shared by every component that reads it.

## Parameters

### key

`string`

### defaultValue

`boolean`

## Returns

`object`

### get

> **get**: () => `boolean`

#### Returns

`boolean`

### set

> **set**: (`next`) => `void`

#### Parameters

##### next

`boolean`

#### Returns

`void`

### use

> **use**: () => `boolean`

#### Returns

`boolean`
