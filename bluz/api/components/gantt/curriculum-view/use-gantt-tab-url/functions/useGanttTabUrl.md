[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/use-gantt-tab-url](../index.md) / useGanttTabUrl

# Function: useGanttTabUrl()

> **useGanttTabUrl**(): \[`number`, `Dispatch`\<`SetStateAction`\<`number`\>\>\]

Defined in: [ui/src/components/gantt/curriculum-view/use-gantt-tab-url.ts:26](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/use-gantt-tab-url.ts#L26)

The selected gantt tab, kept in step with `v=` both ways (#844).

Selecting a tab writes `v=`. Anything else that rewrites the URL — e.g. the
settings dialog's `router.replace`, built from search params read before a
tab switch — moves the tab to match, so the shown tab is always the one a
reload or a shared link would open.

## Returns

\[`number`, `Dispatch`\<`SetStateAction`\<`number`\>\>\]
