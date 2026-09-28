[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/components/insights/build-context](../index.md) / buildInsightContext

# Function: buildInsightContext()

> **buildInsightContext**(`__namedParameters`): [`InsightContext`](../../types/type-aliases/InsightContext.md)

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:115](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L115)

Derives the per-week/day load and a flat, annotated event list once, so the
~40 generators each stay a cheap pass over precomputed arrays.

## Parameters

### \_\_namedParameters

[`BuildInsightContextInput`](../type-aliases/BuildInsightContextInput.md)

## Returns

[`InsightContext`](../../types/type-aliases/InsightContext.md)
