[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/components/insights/generators](../index.md) / partitionInsights

# Function: partitionInsights()

> **partitionInsights**(`insights`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/generators/index.ts:61](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/gantt/curriculum-view/components/insights/generators/index.ts#L61)

Splits the deck for the card (#851): warnings are actionable, so they are
pinned rather than rotated away; trivia always joins the deck.

## Parameters

### insights

readonly [`Insight`](../../types/type-aliases/Insight.md)[]

## Returns

`object`

### deck

> **deck**: [`Insight`](../../types/type-aliases/Insight.md)[]

### pinned

> **pinned**: [`Insight`](../../types/type-aliases/Insight.md)[]
