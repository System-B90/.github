[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/use-grouped-instructors](../index.md) / useGroupedInstructors

# Function: useGroupedInstructors()

> **useGroupedInstructors**(`options?`): [`GroupedInstructors`](../type-aliases/GroupedInstructors.md)

Defined in: [ui/src/components/base/use-grouped-instructors.ts:41](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/use-grouped-instructors.ts#L41)

Groups instructors under the course (מסלול) tree they belong to, walking
parents before children so nested programs read in hierarchy order. Shared by
the instructor select boxes and the schedule instructor rail so both present
the same grouping.

## Parameters

### options?

[`GroupedInstructorsOptions`](../type-aliases/GroupedInstructorsOptions.md) = `{}`

Free-text filter, whether teachers are excluded, and whether
to group at all.

## Returns

[`GroupedInstructors`](../type-aliases/GroupedInstructors.md)

Course-grouped instructors plus the unassigned remainder.
