[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / cutEventFilter

# Function: cutEventFilter()

> **cutEventFilter**(`curriculumId`): `Filter`\<[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)\>

Defined in: [ui/src/api-server/gantt/cut.ts:751](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/cut.ts#L751)

Matches the live (non-archived) schedule events produced by cutting
`curriculumId`. Cut events always store a string `ganttEventId`, so that
`$exists` is what separates them from hand-made events.

Scoping to the curriculum matters when an iteration is relinked from one
curriculum to another — a duplicate of the original, say. "This iteration
holds cut events" was the old test, which reported a never-cut curriculum as
already cut and refused to cut it, purely because the curriculum that used
to be linked had left its events behind (#661).

Events cut before `ganttCurriculumId` was stamped on them carry no curriculum
at all. They still belong to whichever curriculum the iteration is linked to,
so they are matched too — dropping them would make an old cut invisible to
the gate and let it be cut a second time on top of itself.

## Parameters

### curriculumId

`string`

## Returns

`Filter`\<[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)\>
