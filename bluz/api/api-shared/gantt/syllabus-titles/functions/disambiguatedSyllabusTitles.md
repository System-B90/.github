[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/syllabus-titles](../index.md) / disambiguatedSyllabusTitles

# Function: disambiguatedSyllabusTitles()

> **disambiguatedSyllabusTitles**(`syllabuses`, `getCourse`): `Record`\<`string`, `string`\>

Defined in: [ui/src/api-shared/gantt/syllabus-titles.ts:14](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/syllabus-titles.ts#L14)

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
