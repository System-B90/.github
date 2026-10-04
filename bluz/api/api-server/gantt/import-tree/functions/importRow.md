[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/import-tree](../index.md) / importRow

# Function: importRow()

> **importRow**(`table`, `source`, `typeName`, `id`, `now`): `Record`\<`string`, `unknown`\>

Defined in: [ui/src/api-server/gantt/import-tree.ts:52](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/gantt/import-tree.ts#L52)

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
