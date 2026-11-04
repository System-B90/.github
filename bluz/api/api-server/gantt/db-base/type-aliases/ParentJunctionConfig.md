[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-base](../index.md) / ParentJunctionConfig

# Type Alias: ParentJunctionConfig

> **ParentJunctionConfig** = `object`

Defined in: [ui/src/api-server/gantt/db-base.ts:176](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/db-base.ts#L176)

## Properties

### cardinality

> **cardinality**: `"many"` \| `"one"`

Defined in: [ui/src/api-server/gantt/db-base.ts:203](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/db-base.ts#L203)

How many parents a child may have. Every junction table has a composite
`(parent, child)` primary key, so the schema permits many everywhere;
this records the *domain* rule the schema doesn't express.

`"one"` — event→module, module→syllabus, day→week, week→curriculum.
  Surfaced as a scalar id, or `null` when unlinked.
`"many"` — syllabus→curriculum. A syllabus is deliberately shareable
  across curricula (see `addSyllabusToCurriculum`), so collapsing it to
  a scalar would pick an arbitrary parent. Surfaced as a sorted array.

***

### nextSortOrder?

> `optional` **nextSortOrder?**: (`parentId`) => `SQL`

Defined in: [ui/src/api-server/gantt/db-base.ts:209](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/db-base.ts#L209)

`sort_order` expression for a child appended under `parentId`. Set on
ordered junctions so a new child lands last instead of on the column
default (0), which put it first after a reload (#761).

#### Parameters

##### parentId

`string`

#### Returns

`SQL`

***

### outputKey?

> `optional` **outputKey?**: `string`

Defined in: [ui/src/api-server/gantt/db-base.ts:191](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/db-base.ts#L191)

Field name the parent is surfaced under on read. Defaults to
`parentKey`; set it when the read shape differs, e.g. a `"many"`
junction that wants a plural name for its array.

***

### parentKey

> **parentKey**: `string`

Defined in: [ui/src/api-server/gantt/db-base.ts:184](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/db-base.ts#L184)

Column on the junction table holding the parent id. Doubles as the key
`createNewItem` reads the parent out of the create payload, so it must
keep matching the payload field — use `outputKey` to surface it under a
different name.

***

### selfKey

> **selfKey**: `string`

Defined in: [ui/src/api-server/gantt/db-base.ts:185](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/db-base.ts#L185)

***

### table

> **table**: `PgTableWithColumns`\<`any`\>

Defined in: [ui/src/api-server/gantt/db-base.ts:177](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/db-base.ts#L177)
