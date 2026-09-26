[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-fab/curriculum-sync-context](../index.md) / CurriculumSyncContext

# Variable: CurriculumSyncContext

> `const` **CurriculumSyncContext**: `Context`\<`MutableRefObject`\<[`CurriculumSyncHandler`](../type-aliases/CurriculumSyncHandler.md)\> \| `null`\>

Defined in: [ui/src/components/gantt/curriculum-fab/curriculum-sync-context.ts:12](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-fab/curriculum-sync-context.ts#L12)

Lets curriculum-status actions rendered outside the FAB (e.g. the syllabus
tab's about card) push updates into the FAB's own curriculum list cache,
so draft/archive changes made there are reflected in the FAB's grouping.
