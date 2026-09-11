[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/base](../index.md) / ListEntryWithParent

# Type Alias: ListEntryWithParent\<TEntity\>

> **ListEntryWithParent**\<`TEntity`\> = `object` & `Record`\<`string`, `null` \| `string`\>

Defined in: [ui/src/api-client/gantt/base.ts:62](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/base.ts#L62)

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
