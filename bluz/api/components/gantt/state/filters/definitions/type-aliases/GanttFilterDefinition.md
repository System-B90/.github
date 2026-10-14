[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/filters/definitions](../index.md) / GanttFilterDefinition

# Type Alias: GanttFilterDefinition\<K\>

> **GanttFilterDefinition**\<`K`\> = `object`

Defined in: [ui/src/components/gantt/state/filters/definitions.ts:25](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/state/filters/definitions.ts#L25)

One gantt filter: how to tell it is set, whether a syllabus passes it, and
how to phrase it. Adding a filter is a new entry here plus a control in the
popover; the provider ANDs every active definition (#702).

## Type Parameters

### K

`K` *extends* [`GanttFilterKey`](GanttFilterKey.md) = [`GanttFilterKey`](GanttFilterKey.md)

## Properties

### describe

> **describe**: (`value`, `lookups`) => `string`

Defined in: [ui/src/components/gantt/state/filters/definitions.ts:29](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/state/filters/definitions.ts#L29)

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

Defined in: [ui/src/components/gantt/state/filters/definitions.ts:27](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/state/filters/definitions.ts#L27)

#### Parameters

##### value

[`GanttFilterValues`](GanttFilterValues.md)\[`K`\]

#### Returns

`boolean`

***

### key

> **key**: `K`

Defined in: [ui/src/components/gantt/state/filters/definitions.ts:26](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/state/filters/definitions.ts#L26)

***

### matches

> **matches**: (`syllabus`, `value`) => `boolean`

Defined in: [ui/src/components/gantt/state/filters/definitions.ts:28](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/state/filters/definitions.ts#L28)

#### Parameters

##### syllabus

[`GanttSyllabus`](../../../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md)

##### value

[`GanttFilterValues`](GanttFilterValues.md)\[`K`\]

#### Returns

`boolean`
