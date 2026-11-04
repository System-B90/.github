[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/calendar](../index.md) / AiEventSummary

# Type Alias: AiEventSummary

> **AiEventSummary** = `ReturnType`\<*typeof* `summarizeEvent`\>

Defined in: [ui/src/api-server/ai/tools/calendar.ts:51](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/ai/tools/calendar.ts#L51)

Trimmed view of an event — the full document is far too large to re-send,
and a narrow projection means a schema change on the document cannot
silently widen what the assistant sees.

Exported so the benchmark fixture answers with exactly this shape rather
than an approximation of it.
