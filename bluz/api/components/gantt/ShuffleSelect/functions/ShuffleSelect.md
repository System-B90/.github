[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/ShuffleSelect](../index.md) / ShuffleSelect

# Function: ShuffleSelect()

> **ShuffleSelect**(`__namedParameters`): `Element`

Defined in: [ui/src/components/gantt/ShuffleSelect.tsx:14](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/ShuffleSelect.tsx#L14)

Multi-select for tagging a Gantt module/event with shuffle (student group)
names defined on the parent syllabus. An empty selection means the item
applies to all shuffles. Each option shows its Hive student-group
description, when it has one.

## Parameters

### \_\_namedParameters

#### descriptions?

[`ShuffleDescriptions`](../../../../api-shared/gantt/shuffle-names/type-aliases/ShuffleDescriptions.md) = `{}`

The syllabus' shuffle name → description map.

#### onChange

(`shuffles`) => `void`

#### options

`string`[]

Shuffle names defined on the parent syllabus.

#### value

`string`[]

## Returns

`Element`
