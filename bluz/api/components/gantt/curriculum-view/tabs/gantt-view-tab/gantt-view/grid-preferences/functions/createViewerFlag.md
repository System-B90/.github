[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-preferences](../index.md) / createViewerFlag

# Function: createViewerFlag()

> **createViewerFlag**(`key`, `defaultValue`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-preferences.ts:4](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-preferences.ts#L4)

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
