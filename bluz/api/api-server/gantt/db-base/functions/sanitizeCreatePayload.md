[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-base](../index.md) / sanitizeCreatePayload

# Function: sanitizeCreatePayload()

> **sanitizeCreatePayload**(`table`, `data`, `typeName`): `Record`\<`string`, `unknown`\>

Defined in: [ui/src/api-server/gantt/db-base.ts:58](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/gantt/db-base.ts#L58)

Check a create payload against the target table *before* it reaches the
insert, and return only the fields the table actually has.

Without this, an unknown field, a missing NOT NULL column or a bad enum value
all reach the driver and come back as an opaque HTTP 500 (#432, #434).

Unknown fields are dropped rather than rejected: several create payloads
legitimately carry values that live in a junction table instead of on the
entity — and the app itself sends them. A missing required field or a bad enum value, by contrast, is
always a caller mistake, so those become a 400 naming the offending field.

Parent foreign keys (`curriculumId`, `moduleId`, …) live in junction tables
too, so callers must strip them out before calling.

## Parameters

### table

`PgTableWithColumns`\<`any`\>

### data

`Record`\<`string`, `unknown`\>

### typeName

`string`

## Returns

`Record`\<`string`, `unknown`\>
