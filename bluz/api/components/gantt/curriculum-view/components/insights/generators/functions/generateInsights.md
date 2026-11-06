[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/components/insights/generators](../index.md) / generateInsights

# Function: generateInsights()

> **generateInsights**(`ctx`): [`Insight`](../../types/type-aliases/Insight.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/generators/index.ts:36](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/components/gantt/curriculum-view/components/insights/generators/index.ts#L36)

Runs every generator, then orders the deck: warnings first (they are the
point), then the rest with a fun card sprinkled in every few slots so the
humour never clumps. A throwing generator is dropped rather than taking the
whole card down.

## Parameters

### ctx

[`InsightContext`](../../types/type-aliases/InsightContext.md)

## Returns

[`Insight`](../../types/type-aliases/Insight.md)[]
