[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/components/insights/generators](../index.md) / partitionInsights

# Function: partitionInsights()

> **partitionInsights**(`insights`, `__namedParameters`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/generators/index.ts:61](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/components/insights/generators/index.ts#L61)

Splits the deck for the card (#851): warnings are actionable, so they are
pinned rather than rotated away; trivia is opt-in on a work screen.

## Parameters

### insights

readonly [`Insight`](../../types/type-aliases/Insight.md)[]

### \_\_namedParameters

#### includeFun

`boolean`

## Returns

`object`

### deck

> **deck**: [`Insight`](../../types/type-aliases/Insight.md)[]

### pinned

> **pinned**: [`Insight`](../../types/type-aliases/Insight.md)[]
