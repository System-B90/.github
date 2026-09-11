[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/syllabus-card](../index.md) / SyllabusCardProps

# Type Alias: SyllabusCardProps

> **SyllabusCardProps** = `object` & `Omit`\<`CardProps`, `"sx"`\>

Defined in: [ui/src/components/gantt/syllabus-card/index.tsx:27](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/syllabus-card/index.tsx#L27)

Properties for the [SyllabusCard](../functions/SyllabusCard.md) component.

## Type Declaration

### curriculumId

> **curriculumId**: [`GanttCurriculumId`](../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md)

The identifier of the Gantt curriculum context.

### expanded?

> `optional` **expanded?**: `boolean`

Optional controlled expanded state. If provided, the card is controlled.

### onExpandChange?

> `optional` **onExpandChange?**: (`expanded`) => `void`

Optional callback when expansion state changes.

#### Parameters

##### expanded

`boolean`

#### Returns

`void`

### syllabusId

> **syllabusId**: [`GanttSyllabusId`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabusId.md)

The identifier of the syllabus to display.
