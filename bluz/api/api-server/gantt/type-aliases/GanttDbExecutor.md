[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/gantt](../index.md) / GanttDbExecutor

# Type Alias: GanttDbExecutor

> **GanttDbExecutor** = `Parameters`\<`Parameters`\<`PostgresJsDatabase`\<*typeof* [`api-server/gantt/schema`](../schema/index.md)\>\[`"transaction"`\]\>\[`0`\]\>\[`0`\] \| `PostgresJsDatabase`\<*typeof* [`api-server/gantt/schema`](../schema/index.md)\>

Defined in: [ui/src/api-server/gantt/index.ts:44](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/gantt/index.ts#L44)

Anything that can run gantt queries: the pool itself, or a transaction
handle. Helpers accept one so a caller can compose several writes into a
single atomic unit instead of each helper opening its own (#518).
