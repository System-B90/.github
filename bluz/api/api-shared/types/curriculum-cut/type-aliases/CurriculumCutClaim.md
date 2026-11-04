[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/curriculum-cut](../index.md) / CurriculumCutClaim

# Type Alias: CurriculumCutClaim

> **CurriculumCutClaim** = `object`

Defined in: [ui/src/api-shared/types/curriculum-cut.ts:9](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/curriculum-cut.ts#L9)

Ledger row claiming the one-shot cut of a curriculum into an iteration's
calendar. The unique index on `curriculumId` *is* the concurrency control:
the insert, not a lock, decides which of two concurrent cuts proceeds (#515,
the same pattern as `hiveLessonActivations`).

## Properties

### claimedAt

> **claimedAt**: `Date`

Defined in: [ui/src/api-shared/types/curriculum-cut.ts:12](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/curriculum-cut.ts#L12)

When the claim was taken — an audit trail, not a lease.

***

### curriculumId

> **curriculumId**: [`GanttCurriculumId`](../../gantt/models/curriculum/type-aliases/GanttCurriculumId.md)

Defined in: [ui/src/api-shared/types/curriculum-cut.ts:10](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/curriculum-cut.ts#L10)
