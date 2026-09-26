[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/calendar](../index.md) / AiEventSummary

# Type Alias: AiEventSummary

> **AiEventSummary** = `ReturnType`\<*typeof* `summarizeEvent`\>

Defined in: [ui/src/api-server/ai/tools/calendar.ts:85](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/calendar.ts#L85)

Trimmed view of an event — the full document is far too large to re-send,
and a narrow projection means a schema change on the document cannot
silently widen what the assistant sees.

Exported so the benchmark fixture answers with exactly this shape rather
than an approximation of it.
