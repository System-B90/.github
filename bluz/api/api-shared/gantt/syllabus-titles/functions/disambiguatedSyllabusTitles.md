[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/syllabus-titles](../index.md) / disambiguatedSyllabusTitles

# Function: disambiguatedSyllabusTitles()

> **disambiguatedSyllabusTitles**(`syllabuses`, `getCourse`): `Record`\<`string`, `string`\>

Defined in: [ui/src/api-shared/gantt/syllabus-titles.ts:14](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/gantt/syllabus-titles.ts#L14)

Display titles for syllabuses. A title shared by several syllabuses gets its
course names in brackets ("דמות (אפולו)"), so namesakes stay distinguishable.
Unique titles, and syllabuses without a known course, keep the bare title.

## Parameters

### syllabuses

`Iterable`\<`TitledSyllabus`\>

### getCourse

(`id`) => [`Course`](../../../types/course/type-aliases/Course.md) \| `undefined`

## Returns

`Record`\<`string`, `string`\>
