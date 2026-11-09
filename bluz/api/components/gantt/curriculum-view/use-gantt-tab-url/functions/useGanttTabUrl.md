[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/use-gantt-tab-url](../index.md) / useGanttTabUrl

# Function: useGanttTabUrl()

> **useGanttTabUrl**(): \[`number`, `Dispatch`\<`SetStateAction`\<`number`\>\>\]

Defined in: [ui/src/components/gantt/curriculum-view/use-gantt-tab-url.ts:26](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/gantt/curriculum-view/use-gantt-tab-url.ts#L26)

The selected gantt tab, kept in step with `v=` both ways (#844).

Selecting a tab writes `v=`. Anything else that rewrites the URL — e.g. the
settings dialog's `router.replace`, built from search params read before a
tab switch — moves the tab to match, so the shown tab is always the one a
reload or a shared link would open.

## Returns

\[`number`, `Dispatch`\<`SetStateAction`\<`number`\>\>\]
