[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-fab/curriculum-sync-context](../index.md) / CurriculumSyncContext

# Variable: CurriculumSyncContext

> `const` **CurriculumSyncContext**: `Context`\<`MutableRefObject`\<[`CurriculumSyncHandler`](../type-aliases/CurriculumSyncHandler.md)\> \| `null`\>

Defined in: [ui/src/components/gantt/curriculum-fab/curriculum-sync-context.ts:12](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/gantt/curriculum-fab/curriculum-sync-context.ts#L12)

Lets curriculum-status actions rendered outside the FAB (e.g. the syllabus
tab's about card) push updates into the FAB's own curriculum list cache,
so draft/archive changes made there are reflected in the FAB's grouping.
