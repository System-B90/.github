[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/gantt](../index.md) / GanttDbExecutor

# Type Alias: GanttDbExecutor

> **GanttDbExecutor** = `Parameters`\<`Parameters`\<`PostgresJsDatabase`\<*typeof* [`api-server/gantt/schema`](../schema/index.md)\>\[`"transaction"`\]\>\[`0`\]\>\[`0`\] \| `PostgresJsDatabase`\<*typeof* [`api-server/gantt/schema`](../schema/index.md)\>

Defined in: [ui/src/api-server/gantt/index.ts:42](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/index.ts#L42)

Anything that can run gantt queries: the pool itself, or a transaction
handle. Helpers accept one so a caller can compose several writes into a
single atomic unit instead of each helper opening its own (#518).
