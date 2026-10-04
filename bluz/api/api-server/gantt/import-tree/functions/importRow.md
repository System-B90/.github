[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/import-tree](../index.md) / importRow

# Function: importRow()

> **importRow**(`table`, `source`, `typeName`, `id`, `now`): `Record`\<`string`, `unknown`\>

Defined in: [ui/src/api-server/gantt/import-tree.ts:52](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/gantt/import-tree.ts#L52)

Builds an insert row for an exported entity: every real column of the
target table is carried over (recurrence, shuffles, lecturers, room
requirements, …), relational/junction fields (`s2m`, `m2e`) are
dropped by the column filter, enums are validated (bad value → 400), and the
server-owned id/timestamps are replaced.

## Parameters

### table

`PgTableWithColumns`\<`any`\>

### source

`unknown`

### typeName

`string`

### id

`string`

### now

`Date`

## Returns

`Record`\<`string`, `unknown`\>
