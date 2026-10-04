[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/components/insights/build-context](../index.md) / buildInsightContext

# Function: buildInsightContext()

> **buildInsightContext**(`__namedParameters`): [`InsightContext`](../../types/type-aliases/InsightContext.md)

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:111](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L111)

Derives the per-week/day load and a flat, annotated event list once, so the
~40 generators each stay a cheap pass over precomputed arrays.

## Parameters

### \_\_namedParameters

[`BuildInsightContextInput`](../type-aliases/BuildInsightContextInput.md)

## Returns

[`InsightContext`](../../types/type-aliases/InsightContext.md)
