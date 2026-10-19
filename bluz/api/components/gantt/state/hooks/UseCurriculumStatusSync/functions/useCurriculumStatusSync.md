[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/hooks/UseCurriculumStatusSync](../index.md) / useCurriculumStatusSync

# Function: useCurriculumStatusSync()

> **useCurriculumStatusSync**(`curriculumId`): `void`

Defined in: [ui/src/components/gantt/state/hooks/UseCurriculumStatusSync.ts:14](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/gantt/state/hooks/UseCurriculumStatusSync.ts#L14)

Draft/archive status is changed from the curriculum FAB, which only sees the
curriculum list store. Mirror those flags into the open curriculum's own
store so views reading it (e.g. the cut action's draft gate) stay current.

Mount once inside `CurriculumProvider`.

## Parameters

### curriculumId

`string` \| `null`

## Returns

`void`
