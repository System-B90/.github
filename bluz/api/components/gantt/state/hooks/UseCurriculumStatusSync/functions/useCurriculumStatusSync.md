[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/hooks/UseCurriculumStatusSync](../index.md) / useCurriculumStatusSync

# Function: useCurriculumStatusSync()

> **useCurriculumStatusSync**(`curriculumId`): `void`

Defined in: [ui/src/components/gantt/state/hooks/UseCurriculumStatusSync.ts:14](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/state/hooks/UseCurriculumStatusSync.ts#L14)

Draft/archive status is changed from the curriculum FAB, which only sees the
curriculum list store. Mirror those flags into the open curriculum's own
store so views reading it (e.g. the cut action's draft gate) stay current.

Mount once inside `CurriculumProvider`.

## Parameters

### curriculumId

`string` \| `null`

## Returns

`void`
