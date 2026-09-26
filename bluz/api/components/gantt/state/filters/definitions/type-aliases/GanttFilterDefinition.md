[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/filters/definitions](../index.md) / GanttFilterDefinition

# Type Alias: GanttFilterDefinition\<K\>

> **GanttFilterDefinition**\<`K`\> = `object`

Defined in: [ui/src/components/gantt/state/filters/definitions.ts:23](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/filters/definitions.ts#L23)

One gantt filter: how to tell it is set, whether a syllabus passes it, and
how to phrase it. Adding a filter is a new entry here plus a control in the
popover; the provider ANDs every active definition (#702).

## Type Parameters

### K

`K` *extends* [`GanttFilterKey`](GanttFilterKey.md) = [`GanttFilterKey`](GanttFilterKey.md)

## Properties

### describe

> **describe**: (`value`, `lookups`) => `string`

Defined in: [ui/src/components/gantt/state/filters/definitions.ts:27](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/filters/definitions.ts#L27)

#### Parameters

##### value

[`GanttFilterValues`](GanttFilterValues.md)\[`K`\]

##### lookups

[`GanttFilterLookups`](GanttFilterLookups.md)

#### Returns

`string`

***

### isActive

> **isActive**: (`value`) => `boolean`

Defined in: [ui/src/components/gantt/state/filters/definitions.ts:25](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/filters/definitions.ts#L25)

#### Parameters

##### value

[`GanttFilterValues`](GanttFilterValues.md)\[`K`\]

#### Returns

`boolean`

***

### key

> **key**: `K`

Defined in: [ui/src/components/gantt/state/filters/definitions.ts:24](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/filters/definitions.ts#L24)

***

### matches

> **matches**: (`syllabus`, `value`) => `boolean`

Defined in: [ui/src/components/gantt/state/filters/definitions.ts:26](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/filters/definitions.ts#L26)

#### Parameters

##### syllabus

[`GanttSyllabus`](../../../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md)

##### value

[`GanttFilterValues`](GanttFilterValues.md)\[`K`\]

#### Returns

`boolean`
