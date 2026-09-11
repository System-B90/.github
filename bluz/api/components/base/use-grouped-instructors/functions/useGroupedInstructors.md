[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/use-grouped-instructors](../index.md) / useGroupedInstructors

# Function: useGroupedInstructors()

> **useGroupedInstructors**(`options?`): [`GroupedInstructors`](../type-aliases/GroupedInstructors.md)

Defined in: [ui/src/components/base/use-grouped-instructors.ts:37](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/use-grouped-instructors.ts#L37)

Groups instructors under the course (מסלול) tree they belong to, walking
parents before children so nested programs read in hierarchy order. Shared by
the instructor select boxes and the schedule instructor rail so both present
the same grouping.

## Parameters

### options?

[`GroupedInstructorsOptions`](../type-aliases/GroupedInstructorsOptions.md) = `{}`

Free-text filter and whether teachers are excluded.

## Returns

[`GroupedInstructors`](../type-aliases/GroupedInstructors.md)

Course-grouped instructors plus the unassigned remainder.
