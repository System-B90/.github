[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/cut-dialog/cut-target](../index.md) / CutTarget

# Type Alias: CutTarget

> **CutTarget** = \{ `iterationLabel`: `string`; `plannedEvents`: `null` \| `number`; `status`: `"linked"`; \} \| \{ `status`: `"loading"`; \} \| \{ `status`: `"unknown"`; \} \| \{ `status`: `"unlinked"`; \}

Defined in: [ui/src/components/gantt/cut-dialog/cut-target.ts:8](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/gantt/cut-dialog/cut-target.ts#L8)

What the cut dialog knows, before the user presses "גזירה", about where the
cut will land (#838). Resolved when the dialog opens so a missing iteration
link disables the button instead of failing after the click.
