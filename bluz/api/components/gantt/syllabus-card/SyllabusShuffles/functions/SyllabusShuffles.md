[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/syllabus-card/SyllabusShuffles](../index.md) / SyllabusShuffles

# Function: SyllabusShuffles()

> **SyllabusShuffles**(`__namedParameters`): `Element` \| `null`

Defined in: [ui/src/components/gantt/syllabus-card/SyllabusShuffles.tsx:34](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/syllabus-card/SyllabusShuffles.tsx#L34)

Free-text chips editor for the syllabus' shuffle (student group) names.
Modules and events can then be tagged with a subset of these names.

Deleting a name that modules or events still use goes through a confirmation
dialog that lists them and cascades the removal (#485) — otherwise those
items keep a dangling name the UI cannot clear.

## Parameters

### \_\_namedParameters

#### isHovered

`boolean`

#### syllabusId

`string`

## Returns

`Element` \| `null`
