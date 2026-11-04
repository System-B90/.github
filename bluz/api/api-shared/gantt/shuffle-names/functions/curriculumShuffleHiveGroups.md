[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/shuffle-names](../index.md) / curriculumShuffleHiveGroups

# Function: curriculumShuffleHiveGroups()

> **curriculumShuffleHiveGroups**(`syllabuses`): `Map`\<`string`, `number`\>

Defined in: [ui/src/api-shared/gantt/shuffle-names.ts:248](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-shared/gantt/shuffle-names.ts#L248)

Shuffle name → Hive group for a whole curriculum, the way the cut reads it
(#774): the first syllabus that links a name decides, and a syllabus that
leaves it unlinked defers to the others. Every writer of a shuffle-course's
`hiveClassId` goes through this, so a save and a later cut never disagree.

## Parameters

### syllabuses

`object`[]

The curriculum's syllabuses, in curriculum order.

## Returns

`Map`\<`string`, `number`\>

The linked Hive group id per shuffle name.
