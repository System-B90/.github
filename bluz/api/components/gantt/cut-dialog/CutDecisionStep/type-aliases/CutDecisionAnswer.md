[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/cut-dialog/CutDecisionStep](../index.md) / CutDecisionAnswer

# Type Alias: CutDecisionAnswer

> **CutDecisionAnswer** = \{ `acceptedEventIds`: `string`[]; `type`: `"constraint-moves"`; \} \| \{ `acknowledged`: `true`; `type`: `"constraint-violation"`; \} \| \{ `resolution`: [`WeekOverflowResolution`](../../../../../api-shared/gantt/cut-rules/type-aliases/WeekOverflowResolution.md); `type`: `"week-overflow"`; `weekId`: `string`; \}

Defined in: [ui/src/components/gantt/cut-dialog/CutDecisionStep.tsx:24](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/cut-dialog/CutDecisionStep.tsx#L24)

One question from the cut's plan phase, rendered on its own.

Deliberately a single decision per screen: the dialog walks the plan's
`decisions` array one at a time rather than presenting every knob at once,
so the user answers a concrete question about their own schedule instead of
facing a switchboard.
