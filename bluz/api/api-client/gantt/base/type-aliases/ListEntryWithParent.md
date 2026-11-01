[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/base](../index.md) / ListEntryWithParent

# Type Alias: ListEntryWithParent\<TEntity\>

> **ListEntryWithParent**\<`TEntity`\> = `object` & `Record`\<`string`, `null` \| `string`\>

Defined in: [ui/src/api-client/gantt/base.ts:64](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-client/gantt/base.ts#L64)

One entry of `apiListWithParents`: the label plus the entity's parent key
(`syllabusId` on modules, `moduleId` on events, `curriculumId` on
syllabuses/weeks/days), `null` when the child is unlinked. Root entities
(curriculums) carry no parent key at all.

## Type Declaration

### title

> **title**: `TEntity`\[`"title"`\]

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)
