[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/components/insights/build-context](../index.md) / buildInsightContext

# Function: buildInsightContext()

> **buildInsightContext**(`__namedParameters`): [`InsightContext`](../../types/type-aliases/InsightContext.md)

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:111](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L111)

Derives the per-week/day load and a flat, annotated event list once, so the
~40 generators each stay a cheap pass over precomputed arrays.

## Parameters

### \_\_namedParameters

[`BuildInsightContextInput`](../type-aliases/BuildInsightContextInput.md)

## Returns

[`InsightContext`](../../types/type-aliases/InsightContext.md)
