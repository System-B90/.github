[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/calendar](../index.md) / AiEventSummary

# Type Alias: AiEventSummary

> **AiEventSummary** = `ReturnType`\<*typeof* `summarizeEvent`\>

Defined in: [ui/src/api-server/ai/tools/calendar.ts:51](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/ai/tools/calendar.ts#L51)

Trimmed view of an event — the full document is far too large to re-send,
and a narrow projection means a schema change on the document cannot
silently widen what the assistant sees.

Exported so the benchmark fixture answers with exactly this shape rather
than an approximation of it.
