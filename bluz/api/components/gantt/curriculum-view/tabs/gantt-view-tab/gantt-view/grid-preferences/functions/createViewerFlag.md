[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-preferences](../index.md) / createViewerFlag

# Function: createViewerFlag()

> **createViewerFlag**(`key`, `defaultValue`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-preferences.ts:52](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-preferences.ts#L52)

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
