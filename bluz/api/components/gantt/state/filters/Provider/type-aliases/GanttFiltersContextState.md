[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/filters/Provider](../index.md) / GanttFiltersContextState

# Type Alias: GanttFiltersContextState

> **GanttFiltersContextState** = `object`

Defined in: [ui/src/components/gantt/state/filters/Provider.tsx:21](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/filters/Provider.tsx#L21)

## Properties

### clearFilters

> **clearFilters**: () => `void`

Defined in: [ui/src/components/gantt/state/filters/Provider.tsx:24](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/filters/Provider.tsx#L24)

#### Returns

`void`

***

### description

> **description**: `string`

Defined in: [ui/src/components/gantt/state/filters/Provider.tsx:29](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/filters/Provider.tsx#L29)

Human-readable summary of the active filters, empty when none.

***

### hasActiveFilters

> **hasActiveFilters**: `boolean`

Defined in: [ui/src/components/gantt/state/filters/Provider.tsx:25](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/filters/Provider.tsx#L25)

***

### setFilter

> **setFilter**: \<`K`\>(`key`, `value`) => `void`

Defined in: [ui/src/components/gantt/state/filters/Provider.tsx:23](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/filters/Provider.tsx#L23)

#### Type Parameters

##### K

`K` *extends* [`GanttFilterKey`](../../definitions/type-aliases/GanttFilterKey.md)

#### Parameters

##### key

`K`

##### value

[`GanttFilterValues`](../../definitions/type-aliases/GanttFilterValues.md)\[`K`\]

#### Returns

`void`

***

### syllabusMatches

> **syllabusMatches**: (`syllabus`) => `boolean`

Defined in: [ui/src/components/gantt/state/filters/Provider.tsx:27](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/filters/Provider.tsx#L27)

Passes when every active filter matches (AND).

#### Parameters

##### syllabus

[`GanttSyllabus`](../../../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md)

#### Returns

`boolean`

***

### values

> **values**: [`GanttFilterValues`](../../definitions/type-aliases/GanttFilterValues.md)

Defined in: [ui/src/components/gantt/state/filters/Provider.tsx:22](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/filters/Provider.tsx#L22)
