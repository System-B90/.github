[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-base](../index.md) / ParentJunctionConfig

# Type Alias: ParentJunctionConfig

> **ParentJunctionConfig** = `object`

Defined in: [ui/src/api-server/gantt/db-base.ts:170](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/db-base.ts#L170)

## Properties

### cardinality

> **cardinality**: `"many"` \| `"one"`

Defined in: [ui/src/api-server/gantt/db-base.ts:197](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/db-base.ts#L197)

How many parents a child may have. Every junction table has a composite
`(parent, child)` primary key, so the schema permits many everywhere;
this records the *domain* rule the schema doesn't express.

`"one"` — event→module, module→syllabus, day→week, week→curriculum.
  Surfaced as a scalar id, or `null` when unlinked.
`"many"` — syllabus→curriculum. A syllabus is deliberately shareable
  across curricula (see `addSyllabusToCurriculum`), so collapsing it to
  a scalar would pick an arbitrary parent. Surfaced as a sorted array.

***

### outputKey?

> `optional` **outputKey?**: `string`

Defined in: [ui/src/api-server/gantt/db-base.ts:185](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/db-base.ts#L185)

Field name the parent is surfaced under on read. Defaults to
`parentKey`; set it when the read shape differs, e.g. a `"many"`
junction that wants a plural name for its array.

***

### parentKey

> **parentKey**: `string`

Defined in: [ui/src/api-server/gantt/db-base.ts:178](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/db-base.ts#L178)

Column on the junction table holding the parent id. Doubles as the key
`createNewItem` reads the parent out of the create payload, so it must
keep matching the payload field — use `outputKey` to surface it under a
different name.

***

### selfKey

> **selfKey**: `string`

Defined in: [ui/src/api-server/gantt/db-base.ts:179](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/db-base.ts#L179)

***

### table

> **table**: `PgTableWithColumns`\<`any`\>

Defined in: [ui/src/api-server/gantt/db-base.ts:171](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/db-base.ts#L171)
