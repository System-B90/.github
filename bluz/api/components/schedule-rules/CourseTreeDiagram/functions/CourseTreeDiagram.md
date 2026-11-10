[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule-rules/CourseTreeDiagram](../index.md) / CourseTreeDiagram

# Function: CourseTreeDiagram()

> **CourseTreeDiagram**(): `Element`

Defined in: [ui/src/components/schedule-rules/CourseTreeDiagram.tsx:26](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/schedule-rules/CourseTreeDiagram.tsx#L26)

R-53: the course tree. Every student is in Bis90 and in at most one of the
exclusive courses, so their separate syllabuses never constrain each other.
Syllabus membership wins over the tree: a syllabus Apollo and Mivtzar share
has a mix of both courses' shuffles, and those all align.

## Returns

`Element`
