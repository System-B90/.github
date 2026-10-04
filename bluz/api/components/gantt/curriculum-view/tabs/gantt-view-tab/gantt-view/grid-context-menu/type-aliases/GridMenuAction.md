[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-context-menu](../index.md) / GridMenuAction

# Type Alias: GridMenuAction

> **GridMenuAction** = `"clear-week"` \| `"collapse-all-under"` \| `"collapse"` \| `"copy"` \| `"edit-week"` \| `"expand-all-under"` \| `"expand"` \| `"open-dialog"` \| `"remove-mapping"` \| `"set-range"` \| `"split-shuffles"`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-context-menu.ts:8](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-context-menu.ts#L8)

Right-click menu model for the gantt table (#858). Pure, so which entries a
cell offers is testable without rendering the grid; the menu component maps
each id onto the same handlers the keyboard uses.
