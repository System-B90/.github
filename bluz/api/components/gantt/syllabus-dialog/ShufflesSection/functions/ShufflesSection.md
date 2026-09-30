[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/syllabus-dialog/ShufflesSection](../index.md) / ShufflesSection

# Function: ShufflesSection()

> **ShufflesSection**(`__namedParameters`): `Element`

Defined in: [ui/src/components/gantt/syllabus-dialog/ShufflesSection.tsx:288](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/syllabus-dialog/ShufflesSection.tsx#L288)

The syllabus' shuffles (student groups), a section of the syllabus dialog
(#699, folded into the single dialog in #7xx).

Shuffles stay per-syllabus: the names defined here are what the module and
event dialogs offer as tags, and what an event's shuffle group splits across.
Deleting a name that modules or events still use goes through a confirmation
that lists them and cascades the removal (#485) — otherwise those items keep
a dangling name the UI cannot clear.

Each shuffle is a Hive student group: names are offered from Hive, the
description mirrors the group's staff-only description, and a chip shows
whether a same-named group exists (the lesson sync skips shuffles without
one).

## Parameters

### \_\_namedParameters

[`ShufflesSectionProps`](../type-aliases/ShufflesSectionProps.md)

## Returns

`Element`
