[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/cut-dialog/cut-target](../index.md) / CutTarget

# Type Alias: CutTarget

> **CutTarget** = \{ `iterationLabel`: `string`; `plannedEvents`: `null` \| `number`; `status`: `"linked"`; \} \| \{ `status`: `"loading"`; \} \| \{ `status`: `"unknown"`; \} \| \{ `status`: `"unlinked"`; \}

Defined in: [ui/src/components/gantt/cut-dialog/cut-target.ts:8](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/cut-dialog/cut-target.ts#L8)

What the cut dialog knows, before the user presses "גזירה", about where the
cut will land (#838). Resolved when the dialog opens so a missing iteration
link disables the button instead of failing after the click.
