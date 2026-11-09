[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-tab-context](../index.md) / GanttTabContext

# Variable: GanttTabContext

> `const` **GanttTabContext**: `Context`\<[`GanttTabControl`](../type-aliases/GanttTabControl.md) \| `null`\>

Defined in: [ui/src/components/gantt/curriculum-view/gantt-tab-context.ts:14](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/gantt/curriculum-view/gantt-tab-context.ts#L14)

The selected gantt tab, for code inside a tab that must act on its own tab.
Visited tabs stay mounted while hidden (#326), so anything they register
(palette commands) outlives the switch away from them.
